from django import forms
from django.contrib.auth.models import User

from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        help_texts = {
            'username': None,
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('mobileNo', 'location', 'dateofbirth',)
        labels = {
            "mobileNo": "Mobile No.:",
            "location": "Home District:",
            "dateofbirth": "Date of Birth:"
        }
        help_texts = {
            'mobileNo': '<small style="color:teal">not mendatory</small>',
            'location': '<small style="color:teal">not mendatory</small>',
            'dateofbirth': '<small style="color:teal">not mendatory</small>',
        }
        widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}

class profilePicForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_pic',)
        labels = {
            "profile_pic": "Profile Photo:"
        }