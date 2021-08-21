from datetime import date
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

locations = [
    ('Dhaka', 'Dhaka'),
    ('Narayanganj', 'Narayanganj'),
    ('Gazipur', 'Gazipur'),
    ('Cumilla', 'Cumilla'),
    ('Chittagong', 'Chittagong'),
    ('Noakhali', 'Noakhali'),
    ('Jessore', 'Jessore'),
    ('Khulna', 'Khulna'),
    ('Barisal', 'Barisal'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Feni', 'Feni'),
    ('Pabna', 'Pabna'),
    ('Faridpur', 'Faridpur'),
    ('Dinajpur', 'Dinajpur'),
    ('Coxs Bazar', 'Coxs Bazar'),
    ('Bogra', 'Bogra'),
    ('Tangail', 'Tangail'),
    ('Patuakhali', 'Patuakhali'),
    ('Lalmonirhat', 'Lalmonirhat'),
    ('Madaripur', 'Madaripur'),
    ('Naogaon', 'Naogaon'),
    ('Rajbari', 'Rajbari'),
    ('Narail', 'Narail'),
    ('Pirojpur', 'Pirojpur'),
    ('Sherpur', 'Sherpur'),
    ('Mars', 'Mars'),
]

class CustomerProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    currentdate = models.DateField(default=timezone.now)
    location = models.CharField(max_length=30, default='', blank=True, null=True, choices=locations)
    mobileNo = models.CharField(max_length=14, default=None, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles_pic/Customer_profile_pic/', default='/profiles_pic/Customer_profile_pic/demo_profile_pic2.png', blank=True)
    is_customer = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

class AdvertiserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    currentdate = models.DateField(default=timezone.now)
    location = models.CharField(max_length=30, default='', blank=True, null=True, choices=locations)
    mobileNo = models.CharField(max_length=14, default=None, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles_pic/Advertiser_profile_pic/', default='/profiles_pic/Advertiser_profile_pic/demo_profile_pic2.png', blank=True)
    is_advertiser = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

class CityCorporationProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    currentdate = models.DateField(default=timezone.now)
    location = models.CharField(max_length=30, default='', blank=True, null=True, choices=locations)
    mobileNo = models.CharField(max_length=14, default=None, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles_pic/cityCor_profile_pic', default='/profiles_pic/cityCor_profile_pic/demo_profile_pic2.png', blank=True)
    is_cityCor = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)



class PostAdvertiseTable(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length = 100, default=None)
    location = models.CharField(max_length=30, default='', choices=locations)
    Spec_loc = models.CharField(max_length=100, default=None)
    width = models.FloatField(max_length=100, default='0')
    height = models.FloatField(max_length=100, default='0')
    size = models.FloatField(max_length=100, default='0')
    price = models.CharField(max_length=100, default=None)
    short_desc = models.TextField(max_length=1000, default=None)
    post_date = models.DateField(default=timezone.now)
    posted_billboards_pic = models.ImageField(upload_to='posted_billboards_pic/billboards_images',
                                            default='/posted_billboards_pic/billboards_images/demo_billboard_image.JPG',
                                            blank=True)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        self.size = self.width * self.height
        super(PostAdvertiseTable, self).save(*args, **kwargs)

    def __str__(self):
        return self.code


class confirm_post(models.Model):
    confirmed_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    year = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    adCode = models.CharField(max_length=100, unique=True)


class CurrentPriceUpdate(models.Model):
    location = models.CharField(max_length=30, default='', choices=locations)
    current_price = models.FloatField(max_length=10000, default='0')
    update_date = models.DateField(default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return str(self.update_date)







