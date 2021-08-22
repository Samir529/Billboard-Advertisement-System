import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from Billboard_Advertisement.models import CurrentPriceUpdate


class TestViews(TestCase):

    # def setUp(self):
    #     self.update = CurrentPriceUpdate.objects.create(location='Khulna', current_price=15.0, update_date='2021-08-21')

    def test_current_price_update_view_POST(self):
        response = self.client.post(reverse('current_price_update'), {
            'location': 'Khulna',
            'current_price': '12.5',
            'update_date': timezone.now,
        })
        post = CurrentPriceUpdate.objects.last()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(post.location, 'Khulna')
        self.assertEquals(post.current_price, 12.5)
        self.assertEquals(post.update_date, datetime.date.today())
        self.assertTemplateUsed(response, 'update_current_price.html')

    def test_current_price_view_view(self):
        response = self.client.post(reverse('current_price_view'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_current_price.html')

    def test_post_form_view(self):
        response = self.client.get(reverse('post_form'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')

    def test_register_customer_list_view(self):
        response = self.client.get(reverse('register_customer'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'customer_registration.html')

    def test_register_advertiser_list_view(self):
        response = self.client.get(reverse('register_advertiser'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'advertiser_registration.html')

    def test_register_cityCorporation_list_view(self):
        response = self.client.get(reverse('register_cityCorporation'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '')
        self.assertTemplateUsed(response, 'govt_registration.html')


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














