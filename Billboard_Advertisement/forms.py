from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

from .models import CustomerProfileInfo, AdvertiserProfileInfo, CityCorporationProfileInfo, confirm_post, PostAdvertiseTable


class UserForm(forms.ModelForm):
    # password = forms.CharField(min_length=4, widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        help_texts = {
            'username': None,
        }

class customerProfilePicForm(forms.ModelForm):
    class Meta:
        model = CustomerProfileInfo
        fields = ('profile_picture',)
        labels = {
            "profile_picture": "Profile Picture:"
        }

class advertiserProfilePicForm(forms.ModelForm):
    class Meta:
        model = AdvertiserProfileInfo
        fields = ('profile_picture',)
        labels = {
            "profile_picture": "Profile Picture:"
        }

class cityCorporationProfilePicForm(forms.ModelForm):
    class Meta:
        model = CityCorporationProfileInfo
        fields = ('profile_picture',)
        labels = {
            "profile_picture": "Profile Picture:"
        }

class billboardPicForm(forms.ModelForm):
    class Meta:
        model = PostAdvertiseTable
        fields = ('posted_billboards_pic',)
        labels = {
            "posted_billboards_pic": "Billboard Picture:"
        }

class changePassForm(forms.Form):
    old_password_flag = True
    re_new_password_flag = True
    old_password = forms.CharField(label="Old Password", min_length=4, widget=forms.PasswordInput(attrs={'placeholder': ' enter old password'}))
    new_password = forms.CharField(label="New Password", min_length=4, widget=forms.PasswordInput(attrs={'placeholder': ' enter new password'}))
    re_new_password = forms.CharField(label="Re-type New Password", min_length=4,widget=forms.PasswordInput(attrs={'placeholder': ' re-type new password'}))

    def set_old_password_flag(self):
        self.old_password_flag = False

        return 0

    def set_re_new_password_flag(self):
        self.re_new_password_flag = False

        return 0

    def clean_old_password(self, *args, **kwargs):
        old_password = self.cleaned_data.get('old_password')
        if not old_password:
            raise forms.ValidationError("You must enter your old password.")
        if self.old_password_flag == False:
            raise forms.ValidationError("The old password that you have entered is wrong.")
        if self.re_new_password_flag == False:
            raise forms.ValidationError("Re-typed new password did not match with the new password.")

        return old_password

class post_form(forms.ModelForm):
    class Meta:
        model = PostAdvertiseTable
        fields = ('code', 'title', 'location', 'Spec_loc', 'width', 'height', 'price', 'short_desc', 'posted_billboards_pic')
        labels = {
            "code": "Post Code:",
            "title": "Title:",
            "location": "District:",
            "Spec_loc": "Specific Location:",
            "width": "Width of Billboard:",
            "height": "Height of Billboard:",
            "price": "Rent:",
            "short_desc": "Short Description:",
            "posted_billboards_pic": "Billboard Picture:"
        }
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'enter a code'}),
            'title': forms.TextInput(attrs={'placeholder': 'enter title'}),
            'Spec_loc': forms.TextInput(attrs={'placeholder': 'enter specific location'}),
            'width': forms.TextInput(attrs={'placeholder': 'in sq. feet'}),
            'height': forms.TextInput(attrs={'placeholder': 'in sq. feet'}),
            'price': forms.TextInput(attrs={'placeholder': 'enter rent'}),
            'short_desc': forms.Textarea(
                attrs={'rows': 6, 'cols': 50, 'placeholder': 'Write a short description here..'}),
        }

class confirm_post_form(forms.ModelForm):
    dealDuration = forms.DateField(
        initial=timezone.now(),
        widget=forms.SelectDateWidget()
    )
    class Meta:
        model = confirm_post
        dealDuration = forms.DateField(initial=timezone.now())
        fields = ('adCode', 'dealDuration')
        labels = {
            # "year": "Year:",
            # "month": "Month:",
            # "day": "Day:",
            "adCode": "Advertisement Code:",
            "dealDuration": "Deal Duration:",

        }
        widgets = {
            'adCode': forms.TextInput(attrs={'placeholder': ' enter code'}),
        }

    # Check if billboard is already confirmed
    def clean_adCode(self):
        adCode = self.cleaned_data.get("adCode")
        if confirm_post.objects.filter(adCode=adCode).exists():
            raise forms.ValidationError(f"Billboard with code '{adCode}' is already sold!")
        return adCode






# class CustomerProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = CustomerProfileInfo
#         check = forms.BooleanField(required=True)
#         fields = ('mobileNo', 'location', 'Customer_profile_pic', 'is_customer')
#         labels = {
#             "mobileNo": "Mobile No.:",
#             "location": "Location:",
#             # "dateofbirth": "Date of Birth:",
#             "Customer_profile_pic": "Profile Photo:",
#             "check": "Confirm"
#         }
#         help_texts = {
#             'mobileNo': '<small style="color:darkorange">optional</small>',
#             'location': '<small style="color:darkorange">optional</small>',
#             # 'dateofbirth': '<small style="color:darkorange">optional</small>',
#             # 'Customer_profile_pic': '<small style="color:teal">optional</small>',
#             'check': '<small style="color:darkorange">mendatory</small>',
#         }
#         # widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}
#
# class AdvertiserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = AdvertiserProfileInfo
#         check = forms.BooleanField(required=True)
#         fields = ('mobileNo', 'location', 'Advertiser_profile_pic', 'is_advertiser')
#         labels = {
#             "mobileNo": "Mobile No.:",
#             "location": "Location:",
#             # "dateofbirth": "Date of Birth:",
#             "Advertiser_profile_pic": "Profile Photo:",
#             "check": "Confirm"
#         }
#         help_texts = {
#             'mobileNo': '<small style="color:darkorange">optional</small>',
#             'location': '<small style="color:darkorange">optional</small>',
#             # 'dateofbirth': '<small style="color:darkorange">optional</small>',
#             #'Advertiser_profile_pic': '<small style="color:teal">optional</small>',
#             'check': '<small style="color:darkorange">mendatory</small>',
#         }
#         # widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}
#
# class CityCorporationProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = CityCorporationProfileInfo
#         check = forms.BooleanField(required=True)
#         fields = ('mobileNo', 'location', 'cityCor_profile_pic', 'is_cityCor')
#         labels = {
#             "mobileNo": "Mobile No.:",
#             "location": "Location:",
#             # "dateofbirth": "Date of Birth:",
#             "cityCor_profile_pic": "Profile Photo:",
#             "check": "Confirm"
#         }
#         help_texts = {
#             'mobileNo': '<small style="color:darkorange">optional</small>',
#             'location': '<small style="color:darkorange">optional</small>',
#             # 'dateofbirth': '<small style="color:darkorange">optional</small>',
#             #'cityCor_profile_pic': '<small style="color:teal">optional</small>',
#             'check': '<small style="color:darkorange">mendatory</small>',
#         }
#         # widgets = {'dateofbirth': forms.SelectDateWidget(years=range(1900, 2021))}











