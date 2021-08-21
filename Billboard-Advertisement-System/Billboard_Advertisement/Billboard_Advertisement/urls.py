"""Billboard_Advertisement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path
from . import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('register_customer/',views.register_customer,name='register_customer'),
    path('register_advertiser/',views.register_advertiser,name='register_advertiser'),
    path('register_cityCorporation/',views.register_cityCorporation,name='register_cityCorporation'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('adminPanel/',views.adminPanel,name='adminPanel'),
    path('customerPanel/',views.customerPanel,name='customerPanel'),
    path('advertiserPanel/',views.advertiserPanel,name='advertiserPanel'),
    path('cityCorporationPanel/',views.cityCorporationPanel,name='cityCorporationPanel'),
    path('about/',views.about, name="about"),
    path('sign_in_options/',views.sign_in_options, name="sign_in_options"),
    # path('Customer_profile_pic/',views.Customer_profile_pic, name='Customer_profile_pic'),
    # path('Advertiser_profile_pic/',views.Advertiser_profile_pic, name='Advertiser_profile_pic'),
    # path('cityCor_profile_pic/',views.cityCor_profile_pic, name='cityCor_profile_pic'),
    path('post_form/',views.post_form, name='post_form'),
    # path('post_form/post_save',views.post_save, name='post_save'),
    path('sizeMoneyCalculation/', views.sizeMoneyCalculation, name='sizeMoneyCalculation'),
    path('sizeMoneyCalculation/conv/', views.conv, name='conv'),
    path('viewPost/', views.viewPost, name='viewPost'),
    path('postDetail/', views.postDetail, name='postDetail'),
    path('deletePost/', views.deletePost, name='deletePost'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
