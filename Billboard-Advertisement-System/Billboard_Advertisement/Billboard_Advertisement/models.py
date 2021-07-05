from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    # username = models.CharField(max_length=30, default='')
    # first_name = models.CharField(max_length=30, default='')
    # last_name = models.CharField(max_length=30, default='')
    # email = models.EmailField(default='')
    dateofbirth = models.DateField(blank=True,null=True)
    # nid = models.IntegerField(default='0')
    currentdate = models.DateField(default=timezone.now)
    location = models.CharField(max_length=30, default='', blank=True, null=True, choices=locations)
    mobileNo = models.CharField(max_length=11, default='', blank=True, null=True)
    account_age = models.CharField(max_length=10, default='', blank=True, null=True)
    # acc_no = models.IntegerField(default='-', blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profiles_pic', default='/profiles_pic/demo_profile_pic2.png', blank=True)

    def __str__(self):
        return str(self.user)