from django import forms
from django.contrib.auth.models import User

from .models import CustomerProfileInfo, AdvertiserProfileInfo, CityCorporationProfileInfo, Post_Advertise_table


class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=4, widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        help_texts = {
            'username': None,
        }

class CustomerProfileInfoForm(forms.ModelForm):
    class Meta():
        model = CustomerProfileInfo
        is_customer = forms.BooleanField(initial=True)
        fields = ('mobileNo', 'location', 'dateofbirth', 'Customer_profile_pic', 'is_customer')
        labels = {
            "mobileNo": "Mobile No.:",
            "location": "Home District:",
            "dateofbirth": "Date of Birth:",
            "Customer_profile_pic": "Profile Photo:",
            "is_customer": "Is Customer:"
        }
        help_texts = {
            'mobileNo': '<small style="color:darkorange">not mendatory</small>',
            'location': '<small style="color:darkorange">not mendatory</small>',
            'dateofbirth': '<small style="color:darkorange">not mendatory</small>',
            # 'Customer_profile_pic': '<small style="color:teal">not mendatory</small>',
            'is_customer': '<small style="color:darkorange">mendatory</small>',
        }
        widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}

class AdvertiserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = AdvertiserProfileInfo
        is_advertiser = forms.BooleanField(initial=True)
        fields = ('mobileNo', 'location', 'dateofbirth', 'Advertiser_profile_pic', 'is_advertiser')
        labels = {
            "mobileNo": "Mobile No.:",
            "location": "Home District:",
            "dateofbirth": "Date of Birth:",
            "Advertiser_profile_pic": "Profile Photo:",
            "is_advertiser": "Is Advertiser:"
        }
        help_texts = {
            'mobileNo': '<small style="color:darkorange">not mendatory</small>',
            'location': '<small style="color:darkorange">not mendatory</small>',
            'dateofbirth': '<small style="color:darkorange">not mendatory</small>',
            #'Advertiser_profile_pic': '<small style="color:teal">not mendatory</small>',
            'is_advertiser': '<small style="color:darkorange">mendatory</small>',
        }
        widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}

class CityCorporationProfileInfoForm(forms.ModelForm):
    class Meta():
        model = CityCorporationProfileInfo
        is_cityCor = forms.BooleanField(initial=True)
        fields = ('mobileNo', 'location', 'dateofbirth', 'cityCor_profile_pic', 'is_cityCor')
        labels = {
            "mobileNo": "Mobile No.:",
            "location": "Home District:",
            "dateofbirth": "Date of Birth:",
            "cityCor_profile_pic": "Profile Photo:",
            "is_cityCor": "Is Government:"
        }
        help_texts = {
            'mobileNo': '<small style="color:darkorange">not mendatory</small>',
            'location': '<small style="color:darkorange">not mendatory</small>',
            'dateofbirth': '<small style="color:darkorange">not mendatory</small>',
            #'cityCor_profile_pic': '<small style="color:teal">not mendatory</small>',
            'is_cityCor': '<small style="color:darkorange">mendatory</small>',
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

class postedBillboardPicForm(forms.ModelForm):
    class Meta:
        model = Post_Advertise_table
        fields = ('posted_billboards_pic',)
        labels = {
            "posted_billboards_pic": "Billboard Picture:"
        }


class post_from(forms.ModelForm):
    class Meta:
        model = Post_Advertise_table
        fields = ('title', 'Spec_loc', 'size', 'price', 'short_desc', 'posted_billboards_pic')
        labels = {
            "title": "Title:",
            "Spec_loc": "Specific Location:",
            "size": "Size of billboard:",
            "price": "Rent:",
            "short_desc": "Short Description:",
            "posted_billboards_pic": "Billboard Picture:"
        }
















