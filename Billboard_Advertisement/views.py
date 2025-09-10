import copy
import random

from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils import timezone

from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
import datetime

from .filter import billboardFilter, billboardFilter2
from .forms import UserForm, customerProfilePicForm, advertiserProfilePicForm, cityCorporationProfilePicForm, post_form, \
    confirm_post_form, changePassForm, billboardPicForm
from .models import CustomerProfileInfo, CityCorporationProfileInfo, AdvertiserProfileInfo, confirm_post, PostAdvertiseTable, CurrentPriceUpdate


def home(req):
    allPosts = PostAdvertiseTable.objects.all().order_by('-post_date')
    allConfirmedposts = confirm_post.objects.all()

    billboard_filter = billboardFilter2(req.GET, queryset=allPosts)
    context = {'allPosts': allPosts, 'allConfirmedposts': allConfirmedposts, 'filter': billboard_filter}
    return render(req, 'home.html', context)

def base(req):
    return render(req, 'base.html')

def about(request):
    return render(request, 'about.html')

def aboutUs(request):
    return render(request, 'about_us.html')

@login_required
def staffPanel(request):
    return render(request, 'staffPanel.html')

@login_required
def customerPanel(request):
    return render(request, 'Customer_panel.html')

@login_required
def advertiserPanel(request):
    return render(request, 'Advertiser_panel.html')

@login_required
def cityCorporationPanel(request):
    return render(request, 'cityCorporation_panel.html')

def sign_in_options(request):
    if request.method == 'POST':
        if 'Customer' in request.POST:
            return HttpResponseRedirect(reverse('register_customer'))
        elif 'Advertiser' in request.POST:
            return HttpResponseRedirect(reverse('register_advertiser'))
        # elif 'City_Corporation' in request.POST:
        #     return HttpResponseRedirect(reverse('register_cityCorporation'))
    return render(request, 'sign_in_options.html')


def staff_login(request):
    isStaff = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_staff:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return HttpResponseRedirect(reverse('staffPanel'))
            else:
                isStaff = 'not_staff'
                return render(request, 'staff_login.html', {'isStaff': isStaff})
        else:
            isStaff = 'not_user'
            return render(request, 'staff_login.html', {'isStaff': isStaff})
    return render(request, 'staff_login.html', {'isStaff': isStaff})


def user_login(request):
    isuser = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_staff == False:
                if user.is_active:
                    login(request, user)
                    if not remember_me:     # unchecked
                        request.session.set_expiry(0)   # if exits from browser then login will lost,
                                                        # else, if exits from browser then login will not lost
                    try:
                        c = CustomerProfileInfo.objects.get(user=request.user)
                        if c.is_customer==True:
                            return HttpResponseRedirect(reverse('customerPanel'))
                    except CustomerProfileInfo.DoesNotExist:
                        try:
                            a = AdvertiserProfileInfo.objects.get(user=request.user)
                            if a.is_advertiser == True:
                                return HttpResponseRedirect(reverse('advertiserPanel'))
                        except AdvertiserProfileInfo.DoesNotExist:
                            try:
                                ct = CityCorporationProfileInfo.objects.get(user=request.user)
                                if ct.is_cityCor == True:
                                    return HttpResponseRedirect(reverse('cityCorporationPanel'))
                            except CityCorporationProfileInfo.DoesNotExist:
                                return HttpResponse("Account is Not Active.")
                else:
                    return HttpResponse("Account is Not Active.")
            elif user.is_staff == True:
                if user.is_active:
                    isuser = 'staff_user'
                    login(request, user)
                    if not remember_me:
                        request.session.set_expiry(0)
                    return HttpResponseRedirect(reverse('staffPanel'))
                else:
                    return HttpResponse("Account is Not Active.")
        else:
            isuser = 'not_user'

    return render(request, 'user_login.html', {'isuser': isuser})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register_customer(request):
    registered = False
    match_password = 1

    if request.method == 'POST':

        mobileNo = request.POST.get('mobileNo')
        location = request.POST.get('location')

        user_form = UserForm(data=request.POST)
        profile_picture_form = customerProfilePicForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_picture_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            t = CustomerProfileInfo()
            # t2 = User()
            t.mobileNo = mobileNo
            t.location = location
            t.is_customer = True
            t.user = user
            t.profile_picture = profile_picture_form.cleaned_data['profile_picture']
            t.save()
            # t2.username = username
            # t2.password = password
            # t2.first_name = first_name
            # t2.last_name = last_name
            # t2.email = email
            # t2.save()

            registered = True

        elif user_form.data['password'] != user_form.data['confirm_password']:
            # print('password and confirm password does not match')
            match_password = 0
            # user_form.add_error('confirm_password', 'password and confirm password does not match')
        else:
            print(user_form.errors, profile_picture_form.errors)
    else:
        user_form = UserForm()
        profile_picture_form = customerProfilePicForm()
    return render(request, 'customer_registration.html',
            {'user_form': user_form, 'profile_picture_form': profile_picture_form, 'registered': registered, 'match_password': match_password})


def register_advertiser(request):
    registered = False
    match_password = 1

    if request.method == 'POST':

        mobileNo = request.POST.get('mobileNo')
        location = request.POST.get('location')

        user_form = UserForm(data=request.POST)
        profile_picture_form = advertiserProfilePicForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_picture_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            t = AdvertiserProfileInfo()
            t.mobileNo = mobileNo
            t.location = location
            t.is_advertiser = True
            t.user = user
            t.profile_picture = profile_picture_form.cleaned_data['profile_picture']
            t.save()

            registered = True

        elif user_form.data['password'] != user_form.data['confirm_password']:
            # print('password and confirm password does not match')
            match_password = 0
            # user_form.add_error('confirm_password', 'password and confirm password does not match')
        else:
            print(user_form.errors, profile_picture_form.errors)
    else:
        user_form = UserForm()
        profile_picture_form = advertiserProfilePicForm()
    return render(request, 'advertiser_registration.html',
            {'user_form': user_form, 'profile_picture_form': profile_picture_form, 'registered': registered, 'match_password': match_password})


def register_cityCorporation(request):
    registered = False
    match_password = 1

    if request.method == 'POST':

        mobileNo = request.POST.get('mobileNo')
        location = request.POST.get('location')

        user_form = UserForm(data=request.POST)
        profile_picture_form = cityCorporationProfilePicForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_picture_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            t = CityCorporationProfileInfo()
            t.mobileNo = mobileNo
            t.location = location
            t.is_cityCor = True
            t.user = user
            t.profile_picture = profile_picture_form.cleaned_data['profile_picture']
            t.save()

            registered = True

        elif user_form.data['password'] != user_form.data['confirm_password']:
            # print('password and confirm password does not match')
            match_password = 0
            # user_form.add_error('confirm_password', 'password and confirm password does not match')
        else:
            print(user_form.errors, profile_picture_form.errors)
    else:
        user_form = UserForm()
        profile_picture_form = cityCorporationProfilePicForm()
    return render(request, 'govt_registration.html',
            {'user_form': user_form, 'profile_picture_form': profile_picture_form, 'registered': registered, 'match_password': match_password})


@login_required
def updateProfile(request):
    registered = 'no'
    updated = 'no'
    p=0

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobileNo = request.POST.get('mobileNo')
        location = request.POST.get('location')

        if request.user.is_authenticated:
            t = User.objects.get(username=request.user)
            try:
                t2 = CustomerProfileInfo.objects.get(user=request.user)
                if t2.is_customer == True:
                    profile_picture_form = customerProfilePicForm(request.POST, request.FILES)
                    if profile_picture_form.is_valid():
                        profile_pic = profile_picture_form.cleaned_data['profile_picture']
                    else:
                        print(profile_picture_form.errors)
                    if first_name != "":
                        t.first_name = first_name
                    if last_name != "":
                        t.last_name = last_name
                    if email != "":
                        t.email = email
                    if mobileNo != "":
                        t2.mobileNo = mobileNo
                    if location != "":
                        t2.location = location
                    if profile_pic != "/profiles_pic/Customer_profile_pic/demo_profile_pic2.png":
                        t2.profile_picture = profile_pic
                        p=1
                    t.save()
                    t2.save()

            except CustomerProfileInfo.DoesNotExist:
                try:
                    t2 = AdvertiserProfileInfo.objects.get(user=request.user)
                    if t2.is_advertiser == True:
                        profile_picture_form = advertiserProfilePicForm(request.POST, request.FILES)
                        if profile_picture_form.is_valid():
                            profile_pic = profile_picture_form.cleaned_data['profile_picture']
                        else:
                            print(profile_picture_form.errors)
                        if first_name != "":
                            t.first_name = first_name
                        if last_name != "":
                            t.last_name = last_name
                        if email != "":
                            t.email = email
                        if mobileNo != "":
                            t2.mobileNo = mobileNo
                        if location != "":
                            t2.location = location
                        if profile_pic != "/profiles_pic/Advertiser_profile_pic/demo_profile_pic2.png":
                            t2.profile_picture = profile_pic
                            p = 1
                        t.save()
                        t2.save()

                except AdvertiserProfileInfo.DoesNotExist:
                    try:
                        t2 = CityCorporationProfileInfo.objects.get(user=request.user)
                        if t2.is_cityCor == True:
                            profile_picture_form = cityCorporationProfilePicForm(request.POST, request.FILES)
                            if profile_picture_form.is_valid():
                                profile_pic = profile_picture_form.cleaned_data['profile_picture']
                            else:
                                print(profile_picture_form.errors)
                            if first_name != "":
                                t.first_name = first_name
                            if last_name != "":
                                t.last_name = last_name
                            if email != "":
                                t.email = email
                            if mobileNo != "":
                                t2.mobileNo = mobileNo
                            if location != "":
                                t2.location = location
                            if profile_pic != "/profiles_pic/cityCor_profile_pic/demo_profile_pic2.png":
                                t2.profile_picture = profile_pic
                                p = 1
                            t.save()
                            t2.save()

                    except CityCorporationProfileInfo.DoesNotExist:
                        return HttpResponse("Account is Not Actived.")
            if first_name=="" and last_name=="" and email=="" and mobileNo=="" and location=="" and p==0:
                updated = 'all_are_null'
            else:
                updated = 'all_are_not_null'
        else:
            registered = 'not_registered'
    else:
        try:
            t2 = CustomerProfileInfo.objects.get(user=request.user)
            if t2.is_customer == True:
                profile_picture_form = customerProfilePicForm()

        except CustomerProfileInfo.DoesNotExist:
            try:
                t2 = AdvertiserProfileInfo.objects.get(user=request.user)
                if t2.is_advertiser == True:
                    profile_picture_form = advertiserProfilePicForm()

            except AdvertiserProfileInfo.DoesNotExist:
                try:
                    t2 = CityCorporationProfileInfo.objects.get(user=request.user)
                    if t2.is_cityCor == True:
                        profile_picture_form = cityCorporationProfilePicForm()

                except CityCorporationProfileInfo.DoesNotExist:
                    return HttpResponse("Account is Not Active!")
    return render(request, 'update_profile.html', {'profile_picture_form': profile_picture_form, 'registered': registered, 'updated': updated, 't2':t2})


@login_required
def viewProfile(request):
    profile = 0
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        try:
            profile = CustomerProfileInfo.objects.get(user=request.user)
            if profile.is_customer == True:
                confirmed_posts = confirm_post.objects.filter(confirmed_by=user)
                confirmed_post_count = confirmed_posts.count()
                return render(request, 'view_profile.html', {'profile': profile, 'user': user, 'confirmed_post_count': confirmed_post_count})
        except CustomerProfileInfo.DoesNotExist:
            try:
                profile = AdvertiserProfileInfo.objects.get(user=request.user)
                if profile.is_advertiser == True:
                    posts = PostAdvertiseTable.objects.filter(author=user)
                    post_count = posts.count()
                    confirmed_posts = confirm_post.objects.filter(advertiser=user)
                    confirmed_post_count = confirmed_posts.count()
                    return render(request, 'view_profile.html', {'profile': profile, 'user': user, 'post_count': post_count, 'confirmed_post_count': confirmed_post_count})
            except AdvertiserProfileInfo.DoesNotExist:
                try:
                    profile = CityCorporationProfileInfo.objects.get(user=request.user)
                    if profile.is_cityCor == True:
                        return render(request, 'view_profile.html', {'profile': profile, 'user': user})
                except CityCorporationProfileInfo.DoesNotExist:
                    return render(request, 'view_profile.html', {'profile': profile, 'user': user})

    profile = 0
    user = 0
    return render(request, 'view_profile.html', {'profile': profile, 'user': user})

# def change_password(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             t = User.objects.get(username=request.user)
#             form = PasswordChangeForm(t, request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 # update_session_auth_hash(request, user)
#                 # messages.success(request, 'Your password was successfully updated!')
#                 # return redirect('change_password')
#             else:
#                 messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'user/change_password.html', {
#         'form': form
#     })

@login_required
def change_password(request):
    updated = 'no'
    if request.user.is_authenticated:

        form = changePassForm(request.POST or None)

        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        re_new_password = request.POST.get("re_new_password")
        if request.POST.get("old_password"):

            user = User.objects.get(username=request.user.username)

            if user.check_password('{}'.format(old_password)) == False:
                form.set_old_password_flag()
            if re_new_password != new_password:
                form.set_re_new_password_flag()

        if form.is_valid():
            user.set_password('{}'.format(new_password))
            user.save()
            updated = 'yes'
            update_session_auth_hash(request, user)
            # return redirect('change_password')
            return render(request, 'change_password.html', {"form": form, "updated": updated})
        else:
            return render(request, 'change_password.html', {"form": form, "updated": updated})
    else:
        return redirect('user_login')

# @login_required
def current_price_update(request):
    updated = False

    if request.method == 'POST':

        location = request.POST.get('location')
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        t = CurrentPriceUpdate()
        t.location = location
        t.min_price = min_price
        t.max_price = max_price
        t.save()

        updated = True

    return render(request, 'update_current_price.html',{'updated': updated})


def current_price_view(request):
    view_current_price = "xyz"
    if request.method == 'POST':
        location = request.POST.get('location')
        view_current_price = CurrentPriceUpdate.objects.filter(location=location)
        print(view_current_price)
        if not view_current_price:
            view_current_price = "no_data"
        return render(request, 'view_current_price.html', {'filter': view_current_price})

    return render(request, 'view_current_price.html', {'filter': view_current_price})


# @login_required
def advertise_post_form(request):
    form_of_post = post_form(request.POST, request.FILES or None)
    posted = 'no'
    if form_of_post.is_valid():
        instance = form_of_post.save(commit=False)
        instance.author = request.user
        instance.save()
        form_of_post = post_form()
        posted = 'yes'

    context = {
        'form_of_post':form_of_post,
        'posted':posted
    }
    return render(request, 'post_form.html', context)

@login_required
def update_post_form(request):
    registered = 'no'
    updated = 'no'
    different_advertiser = 'no'
    post_code = 1
    p = 0
    billboard_pic_form = billboardPicForm()

    if request.method == 'POST':
        code = request.POST.get('code')
        title = request.POST.get('title')
        location = request.POST.get('location')
        Spec_loc = request.POST.get('Spec_loc')
        width = request.POST.get('width')
        height = request.POST.get('height')
        size = request.POST.get('size')
        price = request.POST.get('price')
        short_desc = request.POST.get('short_desc')

        if request.user.is_authenticated:
            try:
                t = PostAdvertiseTable.objects.get(code=code)

                if t.author == request.user:
                    billboard_pic_form = billboardPicForm(request.POST, request.FILES)
                    if billboard_pic_form.is_valid():
                        billboard_pic = billboard_pic_form.cleaned_data['posted_billboards_pic']
                    else:
                        print(billboard_pic_form.errors)
                    if title != "":
                        t.title = title
                    if location != "":
                        t.location = location
                    if Spec_loc != "":
                        t.Spec_loc = Spec_loc
                    if width != "":
                        t.width = width
                    if height != "":
                        t.height = height
                    if size != "":
                        t.size = size
                    if price != "":
                        t.price = price
                    if short_desc != "":
                        t.short_desc = short_desc
                    if billboard_pic != "/posted_billboards_pic/billboards_images/demo_billboard_image.JPG":
                        t.posted_billboards_pic = billboard_pic
                        p = 1
                    t.save()
                    if title == "" and location == "" and Spec_loc == "" and width == "" and height == "" and size == "" and price == "" and short_desc == "" and p == 0:
                        updated = 'all_are_null'
                    else:
                        updated = 'all_are_not_null'
                else:
                    different_advertiser = 'yes'
            except:
                post_code = 0
        else:
            registered = 'not_registered'

    # else:
    #     billboard_pic_form = billboardPicForm()
    context = {
        'billboard_pic_form': billboard_pic_form,
        'registered': registered,
        'updated': updated,
        'diff_advertiser': different_advertiser,
        'post_code': post_code,
        # 'code': code
    }
    return render(request, 'update_post_form.html', context)



# def post_save(request):
#
#     if request.method == "POST":
#         title = request.POST.get('title')
#         Spec_loc = request.POST.get('location')
#         size = request.POST.get('bill_size')
#         price = request.POST.get('price')
#         short_desc = request.POST.get('desc')
#
#         mydata = Post_Advertise_table()
#
#         mydata.title = title
#         mydata.spec_loc = Spec_loc
#         mydata.size = size
#         mydata.price = price
#         mydata.short_desc = short_desc
#
#         mydata.save()
#         return redirect('advertiserPanel')
#     else:
#
#         return render(request, 'post_form.html')


def sizeMoneyCalculation(request):
    return render(request, 'sizeMoneyCalculation.html')

def conv(request):
    num = "no"
    try:
        val1 = int(request.GET['num1'])
        val2 = int(request.GET['num2'])
    except:
        return render(request, 'convert.html', {'num': num})
    num = "yes"
    res = val1 * val2
    return render(request, 'convert.html', {'result': res, 'size': val2, 'num': num})


@login_required
def viewPost(request):
    allPosts = PostAdvertiseTable.objects.all().order_by('-post_date')
    allConfirmedposts = confirm_post.objects.all()
    profile = 0
    # print(allPosts)
    # print(allConfirmedposts)

    billboard_filter = billboardFilter(request.GET, queryset=allPosts)
    try:
        profile = CustomerProfileInfo.objects.get(user=request.user)
    except CustomerProfileInfo.DoesNotExist:
        try:
            profile = AdvertiserProfileInfo.objects.get(user=request.user)
        except AdvertiserProfileInfo.DoesNotExist:
            try:
                profile = CityCorporationProfileInfo.objects.get(user=request.user)
            except CityCorporationProfileInfo.DoesNotExist:
                msg = "There was an error"
                print(msg)
    has_filter = any(field in request.GET for field in set(billboard_filter.get_fields()))
    if request.method == 'GET':
        if 'all_post' in request.GET:
            all_Posts = PostAdvertiseTable.objects.all().order_by('-post_date')
            billboard_filter = billboardFilter(request.GET, queryset=all_Posts)
        if 'my_post' in request.GET:
            myPosts = PostAdvertiseTable.objects.filter(author=request.user).order_by('-post_date')
            billboard_filter = billboardFilter(request.GET, queryset=myPosts)
        if 'my_deals' in request.GET:
            profile2 = confirm_post.objects.get(confirmed_by=request.user)
            myDeals = PostAdvertiseTable.objects.filter(code=profile2.adCode).order_by('-confirmed_date')
            billboard_filter = billboardFilter(request.GET, queryset=myDeals)
    context = {'allPosts': allPosts, 'allConfirmedposts': allConfirmedposts, 'user': request.user, 'filter': billboard_filter, 'profile': profile}
    # context1 = {'allConfirmedposts': allConfirmedposts}
    return render(request, 'viewPost.html', context)

@login_required
def postDetail(request):
    form_of_post = confirm_post_form(request.POST, request.FILES or None)
    post_code = 1
    posted = 'no'
    msg = 'no'
    profile = 0
    if form_of_post.is_valid():
        try:
            profile = CustomerProfileInfo.objects.get(user=request.user)
            if profile.is_customer == True:
                adCode = form_of_post.cleaned_data['adCode']
                try:
                    code = PostAdvertiseTable.objects.get(code=adCode)
                    instance = form_of_post.save(commit=False)
                    instance.confirmed_by = request.user
                    instance.advertiser = code.author
                    instance.save()
                    form_of_post = confirm_post_form()
                    posted = 'yes'
                except:
                    post_code = 0
        except CustomerProfileInfo.DoesNotExist:
            try:
                profile = AdvertiserProfileInfo.objects.get(user=request.user)
                if profile.is_advertiser == True:
                    msg = "You are an advertiser!"
            except AdvertiserProfileInfo.DoesNotExist:
                try:
                    profile = CityCorporationProfileInfo.objects.get(user=request.user)
                    if profile.is_cityCor == True:
                        msg = "You are city corporation!"
                except CityCorporationProfileInfo.DoesNotExist:
                    msg = "There was an error"
    context = {
        'form_of_post': form_of_post,
        'posted': posted,
        'msg': msg,
        'profile': profile,
        'post_code': post_code
    }
    return render(request, 'postDetail.html', context)

@login_required
def deletePost1(request, c):
    event = PostAdvertiseTable.objects.get(pk=c)
    event.delete()
    # event1=confirm_post.objects.get(adCode=c)
    # event1.delete()

    try:
        # obj = A.objects.get(name='John')
        if confirm_post.objects.filter(adCode=c).exists():
            event1 = confirm_post.objects.get(adCode=c)
            event1.delete()
    except:
        pass

    # event1 = confirm_post.objects.get(pk=code)
    # event1.delete()
    return redirect('viewPost')

# @login_required
# def viewAdvertisersRecords(request):
#     allPosts = PostAdvertiseTable.objects.values('author').distinct()
#     # allConfirmedposts = confirm_post.objects.all()
#
#     return render(request, 'view_advertisers_records.html', {'allPosts': allPosts})

def myPanel(request):
    profile = 0
    if request.user.is_authenticated:
        try:
            profile = CustomerProfileInfo.objects.get(user=request.user)
            if profile.is_customer == True:
                return HttpResponseRedirect(reverse('customerPanel'))
        except CustomerProfileInfo.DoesNotExist:
            try:
                profile = AdvertiserProfileInfo.objects.get(user=request.user)
                if profile.is_advertiser == True:
                    return HttpResponseRedirect(reverse('advertiserPanel'))
            except AdvertiserProfileInfo.DoesNotExist:
                try:
                    profile = CityCorporationProfileInfo.objects.get(user=request.user)
                    if profile.is_cityCor == True:
                        return HttpResponseRedirect(reverse('cityCorporationPanel'))
                except CityCorporationProfileInfo.DoesNotExist:
                    if request.user.is_staff:
                        return HttpResponseRedirect(reverse('staffPanel'))
                    else:
                        msg = "User is not logged in"
                        print(msg)
    else:
        return render(request, 'user_login.html', {'profile': profile})

@login_required
def viewCurrentDealRecords(request):
    allPosts = confirm_post.objects.all()

    return render(request, 'view_current_deal_records.html', {'allPosts': allPosts})

@login_required
def viewAdveriserRecords(request):
    allPosts = AdvertiserProfileInfo.objects.all()

    return render(request, 'view_advertiser_records.html', {'allPosts': allPosts})

@login_required
def viewCustomerRecords(request):
    allPosts = CustomerProfileInfo.objects.all()

    return render(request, 'view_customer_records.html', {'allPosts': allPosts})

def viewRecords(request):
    return render(request, 'view_records.html')































