from django.contrib import admin

# Register your models here.
from .models import CustomerProfileInfo, AdvertiserProfileInfo, CityCorporationProfileInfo

admin.site.register(CustomerProfileInfo)
admin.site.register(AdvertiserProfileInfo)
admin.site.register(CityCorporationProfileInfo)