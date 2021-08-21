from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from django.utils.datetime_safe import datetime

from django.contrib.auth import get_user_model

from Billboard_Advertisement.models import CustomerProfileInfo, AdvertiserProfileInfo, CityCorporationProfileInfo, \
    CurrentPriceUpdate, PostAdvertiseTable


class UserTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='secret', first_name='Samir', last_name='Asif', email='testemail@example.com')

    def test_content(self):
        user = User.objects.get(id=1)
        expected_object_username = f'{user.username}'
        # expected_object_password = f'{user.password}'
        expected_object_first_name = f'{user.first_name}'
        expected_object_last_name = f'{user.last_name}'
        expected_object_email = f'{user.email}'
        self.assertEquals(expected_object_username, 'testuser')
        # self.assertEquals(expected_object_password, 'secret')
        self.assertEquals(self.user.check_password('secret'), True)
        self.assertEquals(expected_object_first_name, 'Samir')
        self.assertEquals(expected_object_last_name, 'Asif')
        self.assertEquals(expected_object_email, 'testemail@example.com')

    def test_is_customer_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_object_name_is_username(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.username}'
        self.assertEqual(str(user), expected_object_name)


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

    def test_customer_list_view(self):
        response = self.client.get(reverse('register_customer'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'customer_registration.html')

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

    def test_customer_list_view(self):
        response = self.client.get(reverse('register_advertiser'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'advertiser_registration.html')

    def test_is_advertiser_label(self):
        user = AdvertiserProfileInfo.objects.get(id=1)
        field_label = user._meta.get_field('is_advertiser').verbose_name
        self.assertEqual(field_label, 'is advertiser')

    def test_mobileNo_max_length(self):
        user = AdvertiserProfileInfo.objects.get(id=1)
        max_length = user._meta.get_field('mobileNo').max_length
        self.assertEqual(max_length, 14)

    def test_object_name_is_user(self):
        user = AdvertiserProfileInfo.objects.get(id=1)
        expected_object_name = f'{user.user}'
        self.assertEqual(str(user), expected_object_name)


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

    def test_customer_list_view(self):
        response = self.client.get(reverse('register_cityCorporation'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'govt_registration.html')

    def test_is_cityCor_label(self):
        user = CityCorporationProfileInfo.objects.get(id=1)
        field_label = user._meta.get_field('is_cityCor').verbose_name
        self.assertEqual(field_label, 'is cityCor')

    def test_mobileNo_max_length(self):
        user = CityCorporationProfileInfo.objects.get(id=1)
        max_length = user._meta.get_field('mobileNo').max_length
        self.assertEqual(max_length, 14)

    def test_object_name_is_user(self):
        user = CityCorporationProfileInfo.objects.get(id=1)
        expected_object_name = f'{user.user}'
        self.assertEqual(str(user), expected_object_name)


# class LoginTest(TestCase):
#     def setUp(self):
#         self.credentials = {
#             'username': 'testuser',
#             'password': 'secret',
#             'first_name': 'Samir',
#             'last_name': 'Asif',
#             'email': 'testemail@example.com'
#         }
#         User.objects.create_user(**self.credentials)
#     def test_login(self):
#         response = self.client.post('/user_login/', self.credentials, follow=True)
#         print(response.context['user'])
#         self.assertTrue(response.context['user'].is_active)



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

    def test_priceUpdate_list_view(self):
        response = self.client.get(reverse('current_price_update'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Dhaka')
        self.assertTemplateUsed(response, 'update_current_price.html')

    def test_update_date_label(self):
        price = CurrentPriceUpdate.objects.get(id=1)
        field_label = price._meta.get_field('update_date').verbose_name
        self.assertEqual(field_label, 'update date')

    def test_current_price_max_length(self):
        price = CurrentPriceUpdate.objects.get(id=1)
        max_length = price._meta.get_field('current_price').max_length
        self.assertEqual(max_length, 10000)

    def test_object_name_is_update_date(self):
        price = CurrentPriceUpdate.objects.get(id=1)
        expected_object_name = f'{price.update_date}'
        self.assertEqual(str(price), expected_object_name)


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

    def test_priceUpdate_list_view(self):
        response = self.client.get(reverse('post_form'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Dhaka')
        self.assertTemplateUsed(response, 'post_form.html')

    def test_Spec_loc_label(self):
        post = PostAdvertiseTable.objects.get(id=1)
        field_label = post._meta.get_field('Spec_loc').verbose_name
        self.assertEqual(field_label, 'Spec loc')

    def test_short_desc_max_length(self):
        post = PostAdvertiseTable.objects.get(id=1)
        max_length = post._meta.get_field('short_desc').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_code(self):
        post = PostAdvertiseTable.objects.get(id=1)
        expected_object_name = f'{post.code}'
        self.assertEqual(str(post), expected_object_name)






























