from django.contrib import admin

# Register your models here.
from .models import CustomerProfileInfo, AdvertiserProfileInfo, CityCorporationProfileInfo, Post_Advertise_table

admin.site.site_header = 'Billboard Advertisement System admin'
admin.site.site_title = 'Billboard Advertisement System admin'
admin.site.index_title = 'Billboard Advertisement System administration'


admin.site.register(CustomerProfileInfo)
admin.site.register(AdvertiserProfileInfo)
admin.site.register(CityCorporationProfileInfo)
admin.site.register(Post_Advertise_table)