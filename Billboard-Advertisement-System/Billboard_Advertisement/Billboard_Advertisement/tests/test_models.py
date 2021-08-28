from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from django.utils.datetime_safe import datetime

from django.contrib.auth import get_user_model

from Billboard_Advertisement.models import CustomerProfileInfo, AdvertiserProfileInfo, CityCorporationProfileInfo, \
    CurrentPriceUpdate, PostAdvertiseTable


class CustomerProfileTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='secret', first_name='Samir', last_name='Asif', email='testemail@example.com')
        CustomerProfileInfo.objects.create(user=self.user, currentdate='2021-08-21', location='Dhaka', mobileNo='+8801845430242', is_customer=True)

    def test_content(self):
        userInfo = CustomerProfileInfo.objects.get(id=1)
        expected_object_user = f'{userInfo.user}'
        expected_object_currentdate = f'{userInfo.currentdate}'
        expected_object_location = f'{userInfo.location}'
        expected_object_mobileNo = f'{userInfo.mobileNo}'
        expected_object_is_customer = f'{userInfo.is_customer}'
        self.assertEquals(expected_object_user, self.user.username)
        self.assertEquals(expected_object_currentdate, '2021-08-21')
        self.assertEquals(expected_object_location, 'Dhaka')
        self.assertEquals(expected_object_mobileNo, '+8801845430242')
        self.assertEquals(expected_object_is_customer, 'True')

    def test_is_customer_label(self):
        user = CustomerProfileInfo.objects.get(id=1)
        field_label = user._meta.get_field('is_customer').verbose_name
        self.assertEqual(field_label, 'is customer')

    def test_mobileNo_max_length(self):
        user = CustomerProfileInfo.objects.get(id=1)
        max_length = user._meta.get_field('mobileNo').max_length
        self.assertEqual(max_length, 14)

    def test_object_name_is_user(self):
        user = CustomerProfileInfo.objects.get(id=1)
        expected_object_name = f'{user.user}'
        self.assertEqual(str(user), expected_object_name)


class AdvertiserProfileTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='secret', first_name='Samir', last_name='Asif', email='testemail@example.com')
        AdvertiserProfileInfo.objects.create(user=self.user, currentdate='2021-08-21', location='Dhaka', mobileNo='+8801845430242', is_advertiser=True)

    def test_content(self):
        userInfo = AdvertiserProfileInfo.objects.get(id=1)
        expected_object_user = f'{userInfo.user}'
        expected_object_currentdate = f'{userInfo.currentdate}'
        expected_object_location = f'{userInfo.location}'
        expected_object_mobileNo = f'{userInfo.mobileNo}'
        expected_object_is_advertiser = f'{userInfo.is_advertiser}'
        self.assertEquals(expected_object_user, self.user.username)
        self.assertEquals(expected_object_currentdate, '2021-08-21')
        self.assertEquals(expected_object_location, 'Dhaka')
        self.assertEquals(expected_object_mobileNo, '+8801845430242')
        self.assertEquals(expected_object_is_advertiser, 'True')


class GovtProfileTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='secret', first_name='Samir', last_name='Asif', email='testemail@example.com')
        CityCorporationProfileInfo.objects.create(user=self.user, currentdate='2021-08-21', location='Dhaka', mobileNo='+8801845430242', is_cityCor=True)

    def test_content(self):
        userInfo = CityCorporationProfileInfo.objects.get(id=1)
        expected_object_user = f'{userInfo.user}'
        expected_object_currentdate = f'{userInfo.currentdate}'
        expected_object_location = f'{userInfo.location}'
        expected_object_mobileNo = f'{userInfo.mobileNo}'
        expected_object_is_cityCor = f'{userInfo.is_cityCor}'
        self.assertEquals(expected_object_user, self.user.username)
        self.assertEquals(expected_object_currentdate, '2021-08-21')
        self.assertEquals(expected_object_location, 'Dhaka')
        self.assertEquals(expected_object_mobileNo, '+8801845430242')
        self.assertEquals(expected_object_is_cityCor, 'True')


class UpdatePriceTest(TestCase):

    def setUp(self):
        CurrentPriceUpdate.objects.create(location='Dhaka', current_price=15.0, update_date='2021-08-21')

    def test_content(self):
        priceUpdate = CurrentPriceUpdate.objects.get(id=1)
        expected_object_location = f'{priceUpdate.location}'
        expected_object_current_price = f'{priceUpdate.current_price}'
        expected_object_update_date = f'{priceUpdate.update_date}'
        self.assertEquals(expected_object_location, 'Dhaka')
        self.assertEquals(expected_object_current_price, '15.0')
        self.assertEquals(expected_object_update_date, '2021-08-21')

    # def test_update_date_label(self):
    #     price = CurrentPriceUpdate.objects.get(id=1)
    #     field_label = price._meta.get_field('update_date').verbose_name
    #     self.assertEqual(field_label, 'update date')

    def test_current_price_max_length(self):
        price = CurrentPriceUpdate.objects.get(id=1)
        max_length = price._meta.get_field('current_price').max_length
        self.assertEqual(max_length, 10000)

    # def test_object_name_is_update_date(self):
    #     price = CurrentPriceUpdate.objects.get(id=1)
    #     expected_object_name = f'{price.update_date}'
    #     self.assertEqual(str(price), expected_object_name)


class PostAdvertiseTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='secret', first_name='Samir', last_name='Asif', email='testemail@example.com')
        PostAdvertiseTable.objects.create(author=self.user, code='ab12', title='ad1', location='Dhaka', Spec_loc='Badda',
                                          width=12.0, height=8.0, size=96.0, price=10.0,
                                          short_desc='abcd', post_date='2021-08-21')

    def test_content(self):
        post = PostAdvertiseTable.objects.get(id=1)
        expected_object_author = f'{post.author}'
        expected_object_code = f'{post.code}'
        expected_object_title = f'{post.title}'
        expected_object_location = f'{post.location}'
        expected_object_Spec_loc = f'{post.Spec_loc}'
        expected_object_width = f'{post.width}'
        expected_object_height = f'{post.height}'
        expected_object_size = f'{post.size}'
        expected_object_price = f'{post.price}'
        expected_object_short_desc = f'{post.short_desc}'
        expected_object_post_date = f'{post.post_date}'
        self.assertEquals(expected_object_author, self.user.username)
        self.assertEquals(expected_object_code, 'ab12')
        self.assertEquals(expected_object_title, 'ad1')
        self.assertEquals(expected_object_location, 'Dhaka')
        self.assertEquals(expected_object_Spec_loc, 'Badda')
        self.assertEquals(expected_object_width, '12.0')
        self.assertEquals(expected_object_height, '8.0')
        self.assertEquals(expected_object_size, '96.0')
        self.assertEquals(expected_object_price, '10.0')
        self.assertEquals(expected_object_short_desc, 'abcd')
        self.assertEquals(expected_object_post_date, '2021-08-21')

    # def test_Spec_loc_label(self):
    #     post = PostAdvertiseTable.objects.get(id=1)
    #     field_label = post._meta.get_field('Spec_loc').verbose_name
    #     self.assertEqual(field_label, 'Spec loc')

    def test_short_desc_max_length(self):
        post = PostAdvertiseTable.objects.get(id=1)
        max_length = post._meta.get_field('short_desc').max_length
        self.assertEqual(max_length, 500)

    # def test_object_name_is_code(self):
    #     post = PostAdvertiseTable.objects.get(id=1)
    #     expected_object_name = f'{post.code}'
    #     self.assertEqual(str(post), expected_object_name)






























