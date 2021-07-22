import copy
import random

from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
import datetime

from .forms import CustomerProfileInfoForm, UserForm, AdvertiserProfileInfoForm, CityCorporationProfileInfoForm, \
    customerProfilePicForm, advertiserProfilePicForm, cityCorporationProfilePicForm, post_from
from .models import CustomerProfileInfo, CityCorporationProfileInfo, AdvertiserProfileInfo, Post_Advertise_table


def home(req):
    return render(req, 'home.html')

def base(req):
    return render(req, 'base.html')

def adminPanel(request):
    return render(request, 'adminPanel.html')

def customerPanel(request):
    return render(request, 'Customer_panel.html')

def advertiserPanel(request):
    return render(request, 'Advertiser_panel.html')

def cityCorporationPanel(request):
    return render(request, 'cityCorporation_panel.html')

def sign_in_options(request):
    if request.method == 'POST':
        if 'Customer' in request.POST:
            return HttpResponseRedirect(reverse('register_customer'))
        elif 'Advertiser' in request.POST:
            return HttpResponseRedirect(reverse('register_advertiser'))
        elif 'City_Corporation' in request.POST:
            return HttpResponseRedirect(reverse('register_cityCorporation'))
    return render(request, 'sign_in_options.html')


def admin_login(request):
    isadmin = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_superuser:
                return HttpResponseRedirect(reverse('adminPanel'))

            else:
                isadmin = 'b'
                return render(request, 'admin_login.html',{'isadmin': isadmin})
        else:
            isadmin = 'c'
            return render(request, 'admin_login.html', {'isadmin': isadmin})
    return render(request, 'admin_login.html', {'isadmin': isadmin})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register_customer(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = CustomerProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = CustomerProfileInfoForm()
    return render(request, 'customer_registration.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def register_advertiser(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = AdvertiserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = AdvertiserProfileInfoForm()
    return render(request, 'advertiser_registration.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def register_cityCorporation(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = CityCorporationProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = CityCorporationProfileInfoForm()
    return render(request, 'govt_registration.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):
    isuser = 'a'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
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
                            return HttpResponse("Account not actived.")
            else:
                return HttpResponse("Account not actived.")
        else:
            isuser = 'b'
            return render(request, 'user_login.html',{'isuser': isuser})

    return render(request, 'user_login.html', {'isuser': isuser})



def about(request):
    return render(request, 'about.html')

def Customer_profile_pic(request):
    if request.method == 'POST':
        form = customerProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            t = CustomerProfileInfo.objects.get(user=request.user)
            t.profile_pic = form.cleaned_data['profile_pic']
            t.save()
            #img_obj = form.instance
            return render(request, 'profile_pic.html', {'form': form, 't': t})
    else:
        form = customerProfilePicForm()
    return render(request, 'profile_pic.html', {'form': form})

def Advertiser_profile_pic(request):
    if request.method == 'POST':
        form = advertiserProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            t = AdvertiserProfileInfo.objects.get(user=request.user)
            t.profile_pic = form.cleaned_data['profile_pic']
            t.save()
            #img_obj = form.instance
            return render(request, 'profile_pic.html', {'form': form, 't': t})
    else:
        form = advertiserProfilePicForm()
    return render(request, 'profile_pic.html', {'form': form})

def cityCor_profile_pic(request):
    if request.method == 'POST':
        form = cityCorporationProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            t = CityCorporationProfileInfo.objects.get(user=request.user)
            t.profile_pic = form.cleaned_data['profile_pic']
            t.save()
            #img_obj = form.instance
            return render(request, 'profile_pic.html', {'form': form, 't': t})
    else:
        form = cityCorporationProfilePicForm()
    return render(request, 'profile_pic.html', {'form': form})


def post_form(request):
    form_of_post = post_from(request.POST or None)
    if form_of_post.is_valid():
        form_of_post.save()
        form_of_post = post_from()

    context = {
        'form_of_post':form_of_post
    }
    return render(request, 'post_form.html', context)

def post_save(request):

    if request.method == "POST":
        title = request.POST.get('title')
        Spec_loc = request.POST.get('location')
        size = request.POST.get('bill_size')
        price = request.POST.get('price')
        short_desc = request.POST.get('desc')

        mydata = Post_Advertise_table()

        mydata.title = title
        mydata.spec_loc = Spec_loc
        mydata.size = size
        mydata.price = price
        mydata.short_desc = short_desc

        mydata.save()
        return redirect('advertiserPanel')
    else:

        return render(request, 'post_form.html')




def sizeMoneyCalculation(request):
    return render(request, 'sizeMoneyCalculation.html')


def conv(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 * val2
    return render(request, 'convert.html', {'result': res, 'size': val2})















































