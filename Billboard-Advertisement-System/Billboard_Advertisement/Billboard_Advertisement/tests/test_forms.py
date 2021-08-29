from django.contrib.auth import get_user_model
from django.test import TestCase

from Billboard_Advertisement.forms import confirm_post_form, post_form, changePassForm, customerProfilePicForm, UserForm


class TestForms(TestCase):
    #databases = '__all__'
    def test_confirm_post_form_valid_data(self):
        form = confirm_post_form(data={
            'year': '2021',
            'month': 'January',
            'day': '01',
            'adCode': '0013',

        })
        self.assertTrue(form.is_valid())

    def test_confirm_post_form_no_data(self):
        form = confirm_post_form(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),4)


    def test_post_form_valid_data(self):
        form = post_form(data = {
            'code': "0013",
            'title': "title",
            'location': "Dhaka",
            'Spec_loc': "Jatrabari",
            'width': "12.0",
            'height': "8.0",
            'price': "1000",
            'short_desc': "This is billboard",
            'posted_billboards_pic': "Billboard Picture"
        })
        self.assertTrue(form.is_valid())

    def test_post_from_form_no_data(self):
        form = post_form(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),8)


    def test_changePassword_from_valid_data(self):
        form = changePassForm(data = {
            'old_password': "1234",
            'new_password': "abcd",
            're_new_password': "abcd",
        })
        self.assertTrue(form.is_valid())

    def test_changePassword_form_no_data(self):
        form = changePassForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),3)




    # def test_user_from_valid_data(self):
    #     form = UserForm(data = {
    #         'username': "testuser",
    #         'password': "abcd1234",
    #         'first_name': "Samir",
    #         'last_name': "Asif",
    #         'email': "testemail@example.com",
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_user_form_no_data(self):
    #     form = UserForm(data={})
    #
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(len(form.errors),2)

    # def test_profilePic_from_valid_data(self):
    #     form = customerProfilePicForm(data = {
    #         'profile_picture': "Profile Picture",
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_profilePic_form_no_data(self):
    #     form = customerProfilePicForm(data={})
    #
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(len(form.errors),1)














