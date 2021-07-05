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

from django.shortcuts import render
import datetime

from .forms import UserProfileInfoForm, UserForm


def home(req):
    return render(req, 'home.html')

def base(req):
    return render(req, 'base.html')

def adminPanel(request):
    return render(request, 'adminPanel.html')


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


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

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
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
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
                return HttpResponseRedirect(reverse('home'))    ##

            else:
                return HttpResponse("Account not actived.")
        else:
            isuser = 'b'
            return render(request, 'user_login.html',{'isuser': isuser})

    return render(request, 'user_login.html', {'isuser': isuser})


def about(request):
    return render(request, 'about.html')