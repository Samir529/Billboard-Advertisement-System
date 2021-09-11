
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Billboard_Advertisement.views import register_customer, home, sizeMoneyCalculation, viewPost, postDetail, \
    advertise_post_form


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_register_customer_url_is_resolved(self):
        url = reverse('register_customer')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_customer)


    def test_sizeMoneyCalculation_url_is_resolved(self):
        url = reverse('sizeMoneyCalculation')
        print(resolve(url))
        self.assertEquals(resolve(url).func, sizeMoneyCalculation)

    def test_viewPost_url_is_resolved(self):
        url = reverse('viewPost')
        print(resolve(url))
        self.assertEquals(resolve(url).func, viewPost)

    def test_post_form_is_resolved(self):
        url = reverse('advertise_post_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func, advertise_post_form)

    def test_postDetail_is_resolved(self):
        url = reverse('postDetail')
        print(resolve(url))
        self.assertEquals(resolve(url).func, postDetail)






