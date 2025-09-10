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
    path('about/',views.about, name="about"),
    path('aboutUs/',views.aboutUs, name="aboutUs"),
    path('base/',views.base,name='base'),
    path('register_customer/',views.register_customer,name='register_customer'),
    path('register_advertiser/',views.register_advertiser,name='register_advertiser'),
    path('register_cityCorporation/',views.register_cityCorporation,name='register_cityCorporation'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('staffPanel/', views.staffPanel, name='staffPanel'),
    path('customerPanel/',views.customerPanel,name='customerPanel'),
    path('advertiserPanel/',views.advertiserPanel,name='advertiserPanel'),
    path('cityCorporationPanel/',views.cityCorporationPanel,name='cityCorporationPanel'),
    path('sign_in_options/',views.sign_in_options, name="sign_in_options"),
    path('update_profile/',views.updateProfile, name='updateProfile'),
    path('view_profile/',views.viewProfile, name='viewProfile'),
    path('password/',views.change_password, name='change_password'),
    path('advertise_post_form/',views.advertise_post_form, name='advertise_post_form'),
    path('update_post_form/',views.update_post_form, name='update_post_form'),
    # path('post_form/post_save',views.post_save, name='post_save'),
    path('sizeMoneyCalculation/', views.sizeMoneyCalculation, name='sizeMoneyCalculation'),
    path('sizeMoneyCalculation/conv/', views.conv, name='conv'),
    path('viewPost/', views.viewPost, name='viewPost'),
    path('postDetail/', views.postDetail, name='postDetail'),
    #path('deletePost/', views.deletePost, name='deletePost'),
    path('deletePost1/<c>', views.deletePost1, name='deletePost1'),
    path('current_price_update/',views.current_price_update, name='current_price_update'),
    path('current_price_view/',views.current_price_view, name='current_price_view'),
    # path('viewAdvertisersRecords/',views.viewAdvertisersRecords, name='viewAdvertisersRecords'),
    path('myPanel/',views.myPanel, name='myPanel'),
    path('viewCurrentDealRecords/',views.viewCurrentDealRecords, name='viewCurrentDealRecords'),
    path('viewAdveriserRecords/',views.viewAdveriserRecords, name='viewAdveriserRecords'),
    path('viewCustomerRecords/',views.viewCustomerRecords, name='viewCustomerRecords'),
    path('viewRecords/',views.viewRecords, name='viewRecords'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



