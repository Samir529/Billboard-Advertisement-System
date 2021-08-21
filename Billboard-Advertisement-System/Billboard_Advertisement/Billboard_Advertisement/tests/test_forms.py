from django.test import TestCase

from Billboard_Advertisement.forms import confirm_post_form, post_from


class TestForms(TestCase):
    #databases = '__all__'
    def test_confirm_post_form_valid_data(self):
        form = confirm_post_form(data={
            'year': '2021',
            'month': 'January',
            'day': '01',
            'adCode': '001',

        })

        self.assertTrue(form.is_valid())

    def test_confirm_post_form_no_data(self):
        form = confirm_post_form(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),4)


    def test_post_from_valid_data(self):
        form = post_from(data = {
            'code': '001',
            'title': "title",
            'Spec_loc': "Jatrabari",
            'size': "30x30",
            'price': "1000",
            'short_desc': "This is billboard",
            'posted_billboards_pic': "Billboard Picture"
        })
        self.assertTrue(form.is_valid())


    def test_post_from_form_no_data(self):
        form = post_from(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),6)


