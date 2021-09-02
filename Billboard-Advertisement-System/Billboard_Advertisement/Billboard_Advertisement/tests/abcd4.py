# class TestUrls(SimpleTestCase):
#
#     def test_plasma_donation_home_view_url_is_resolved(self):
#         url = reverse('plasma-donation-home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, plasma_donation_home_view)
#
#     def test_post_plasma_request_view_url_is_resolved(self):
#         url = reverse('plasma-donation-post-request')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, post_plasma_request_view)
#
#     def test_update_plasma_request_view_url_is_resolved(self):
#         url = reverse('plasma-donation-update-request')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, update_plasma_request_view)
#
#     def test_delete_plasma_request_view_url_is_resolved(self):
#         url = reverse('plasma-donation-delete-request')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, delete_plasma_request_view)
#
#     def test_plasma_request_detail_view_url_is_resolved(self):
#         url = reverse('plasma-donation-request-detail')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, plasma_request_detail_view)
#
#     def test_users_requests_view_url_is_resolved(self):
#         url = reverse('users-plasma-requests')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, users_requests_view)
#
#
# class TestForms(SimpleTestCase):
#
#     def test_PlasmaRequestForm_from_valid_data(self):
#         form = PlasmaRequestForm(data={
#             'gender': "Male",
#             'blood_group': "A+",
#             'needed_within': "2021-09-01",
#         })
#         self.assertTrue(form.is_valid())
#
#     def test_PlasmaRequestForm_form_no_data(self):
#         form = PlasmaRequestForm(data={})
#
#         self.assertFalse(form.is_valid())
#         self.assertEqual(len(form.errors), 3)
#
#
# class PlasmaRequestModelTest(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='testuser', password='secret', first_name='fname', last_name='lname',
#             email='testemail@example.com')
#         PlasmaRequestModel.objects.create(user=self.user, patient_name='test_name', gender='test_gender',
#                                           blood_group='A+', quantity=2, location='Dhaka', is_emergency=True,
#                                           is_active=True, needed_within='2021-09-01', phone='017xxxxxxxx',
#                                           note='test_note', posted_on='2021-09-01')
#
#     def test_content(self):
#         post = PlasmaRequestModel.objects.get(id=1)
#         expected_object_user = f'{post.user}'
#         expected_object_patient_name = f'{post.patient_name}'
#         expected_object_gender = f'{post.gender}'
#         expected_object_blood_group = f'{post.blood_group}'
#         expected_object_quantity = f'{post.quantity}'
#         expected_object_location = f'{post.location}'
#         expected_object_is_emergency = f'{post.is_emergency}'
#         expected_object_is_active = f'{post.is_active}'
#         expected_object_needed_within = f'{post.needed_within}'
#         expected_object_phone = f'{post.phone}'
#         expected_object_note = f'{post.note}'
#         expected_object_posted_on = f'{post.posted_on}'
#         self.assertEquals(expected_object_user, self.user.username)
#         self.assertEquals(expected_object_patient_name, 'test_name')
#         self.assertEquals(expected_object_gender, 'test_gender')
#         self.assertEquals(expected_object_blood_group, 'A+')
#         self.assertEquals(expected_object_quantity, '2')
#         self.assertEquals(expected_object_location, 'Dhaka')
#         self.assertEquals(expected_object_is_emergency, 'True')
#         self.assertEquals(expected_object_is_active, 'True')
#         self.assertEquals(expected_object_needed_within, '2021-09-01')
#         self.assertEquals(expected_object_phone, '017xxxxxxxx')
#         self.assertEquals(expected_object_note, 'test_note')
#         self.assertEquals(expected_object_posted_on, '2021-09-01')
#
#
#
