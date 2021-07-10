from django import forms
from django.contrib.auth.models import User

from .models import CustomerProfileInfo, AdvertiserProfileInfo, CityCorporationProfileInfo, Post_Advertise_table


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        help_texts = {
            'username': None,
        }

class CustomerProfileInfoForm(forms.ModelForm):
    class Meta():
        model = CustomerProfileInfo
        fields = ('mobileNo', 'location', 'dateofbirth', 'Customer_profile_pic')
        labels = {
            "mobileNo": "Mobile No.:",
            "location": "Home District:",
            "dateofbirth": "Date of Birth:",
            "Customer_profile_pic": "Profile Photo:"
        }
        help_texts = {
            'mobileNo': '<small style="color:teal">not    mendatory</small>',
            'location': '<small style="color:teal">not mendatory</small>',
            'dateofbirth': '<small style="color:teal">not mendatory</small>',
            #'Customer_profile_pic': '<small style="color:teal">not mendatory</small>',
        }
        widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}

class AdvertiserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = AdvertiserProfileInfo
        fields = ('mobileNo', 'location', 'dateofbirth', 'Advertiser_profile_pic')
        labels = {
            "mobileNo": "Mobile No.:",
            "location": "Home District:",
            "dateofbirth": "Date of Birth:",
            "Advertiser_profile_pic": "Profile Photo:"
        }
        help_texts = {
            'mobileNo': '<small style="color:teal">not mendatory</small>',
            'location': '<small style="color:teal">not mendatory</small>',
            'dateofbirth': '<small style="color:teal">not mendatory</small>',
            #'Advertiser_profile_pic': '<small style="color:teal">not mendatory</small>',
        }
        widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}

class CityCorporationProfileInfoForm(forms.ModelForm):
    class Meta():
        model = CityCorporationProfileInfo
        fields = ('mobileNo', 'location', 'dateofbirth', 'cityCor_profile_pic')
        labels = {
            "mobileNo": "Mobile No.:",
            "location": "Home District:",
            "dateofbirth": "Date of Birth:",
            "cityCor_profile_pic": "Profile Photo:"
        }
        help_texts = {
            'mobileNo': '<small style="color:teal">not mendatory</small>',
            'location': '<small style="color:teal">not mendatory</small>',
            'dateofbirth': '<small style="color:teal">not mendatory</small>',
            #'cityCor_profile_pic': '<small style="color:teal">not mendatory</small>',
        }
        widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}

class customerProfilePicForm(forms.ModelForm):
    class Meta:
        model = CustomerProfileInfo
        fields = ('Customer_profile_pic',)
        labels = {
            "Customer_profile_pic": "Profile Photo:"
        }

class advertiserProfilePicForm(forms.ModelForm):
    class Meta:
        model = AdvertiserProfileInfo
        fields = ('Advertiser_profile_pic',)
        labels = {
            "Advertiser_profile_pic": "Profile Photo:"
        }

class cityCorporationProfilePicForm(forms.ModelForm):
    class Meta:
        model = CityCorporationProfileInfo
        fields = ('cityCor_profile_pic',)
        labels = {
            "cityCor_profile_pic": "Profile Photo:"
        }



class post_from(forms.ModelForm):
    class Meta:
        model = Post_Advertise_table
        fields = ('title', 'Spec_loc', 'size', 'price', 'short_desc')
        labels = {
            "title": "Title: ",
            "Spec_loc": "Specific Location: ",
            "size": "Size of billboard: ",
            "price": "Price: ",
            "short_desc": "Short Description: "
        }
















