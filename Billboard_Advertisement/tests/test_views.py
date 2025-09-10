import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from Billboard_Advertisement.models import CurrentPriceUpdate, PostAdvertiseTable, CustomerProfileInfo


class TestViews(TestCase):

    # def setUp(self):
    #     self.user = get_user_model().objects.create_user(
    #         username='testuser', password='secret', first_name='Samir', last_name='Asif', email='testemail@example.com')
    #
    #     self.update = CurrentPriceUpdate.objects.create(location='Khulna', min_price=15.0, max_price=15.0, update_date='2021-08-21')

    def test_current_price_update_view_POST(self):
        response = self.client.post(reverse('current_price_update'), data={
            'location': 'Khulna',
            'min_price': '12.5',
            'max_price': '16.5',
            'update_date': timezone.now,
        })
        post = CurrentPriceUpdate.objects.last()
        self.assertEqual(CurrentPriceUpdate.objects.count(), 1)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(post.location, 'Khulna')
        self.assertEquals(post.min_price, 12.5)
        self.assertEquals(post.max_price, 16.5)
        self.assertEquals(post.update_date, datetime.date.today())
        self.assertTemplateUsed(response, 'update_current_price.html')

    def test_current_price_view_view(self):
        response = self.client.post(reverse('current_price_view'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_current_price.html')

    def test_advertise_post_form_view(self):
        response = self.client.get(reverse('advertise_post_form'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')

    def test_register_customer_view(self):
        response = self.client.get(reverse('register_customer'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'customer_registration.html')

    def test_register_advertiser_view(self):
        response = self.client.get(reverse('register_advertiser'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'advertiser_registration.html')

    def test_register_cityCorporation_view(self):
        response = self.client.get(reverse('register_cityCorporation'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'govt_registration.html')








    # def test_advertise_post_form_view_POST(self):
    #     response = self.client.post(reverse('advertise_post_form'), data={
    #         'code': "0013",
    #         'title': "test_title",
    #         'location': "Dhaka",
    #         'Spec_loc': "Badda",
    #         'width': "12.0",
    #         'height': "8.0",
    #         'price': "1000",
    #         'short_desc': "This is a billboard",
    #         'posted_billboards_pic': "/posted_billboards_pic/billboards_images/demo_billboard_image.JPG"
    #     })
    #     post = PostAdvertiseTable.objects.last()
    #     self.assertEqual(PostAdvertiseTable.objects.count(), 1)
    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals(post.code, '0013')
    #     self.assertEquals(post.title, 'test_title')
    #     self.assertEquals(post.location, 'Badda')
    #     self.assertEquals(post.width, 12.0)
    #     self.assertEquals(post.height, 8.0)
    #     self.assertEquals(post.price, 1000)
    #     self.assertEquals(post.short_desc, 'This is a billboard')
    #     self.assertEquals(post.posted_billboards_pic, "/posted_billboards_pic/billboards_images/demo_billboard_image.JPG")
    #     self.assertTemplateUsed(response, 'post_form.html')


    # def test_register_customer_view_POST(self):
    #     response = self.client.post(reverse('register_customer'), data={
    #         'user': self.user.username,
    #         'location': "Dhaka",
    #         'mobileNo': "+8801845430242",
    #         'is_customer': True,
    #         'profile_picture': "/profiles_pic/cityCor_profile_pic/demo_profile_pic2.png"
    #     })
    #     post = CustomerProfileInfo.objects.last()
    #     self.assertEqual(CustomerProfileInfo.objects.count(), 1)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertEquals(post.user, self.user.username)
    #     self.assertEquals(post.location, 'Dhaka')
    #     self.assertEquals(post.mobileNo, '+8801845430242')
    #     self.assertEquals(post.is_customer, 'True')
    #     self.assertEquals(post.profile_picture, "/profiles_pic/cityCor_profile_pic/demo_profile_pic2.png")
    #     self.assertTemplateUsed(response, 'customer_registration.html')


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












