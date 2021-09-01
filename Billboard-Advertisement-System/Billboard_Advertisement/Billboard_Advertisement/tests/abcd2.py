# class TestUrls(SimpleTestCase):
#
#     def test_health_record_home_view_url_is_resolved(self):
#         url = reverse('health-record-home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, health_record_home_view)
#
#     def test_health_record_create_view_url_is_resolved(self):
#         url = reverse('health-record-home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, health_record_create_view)
#
#     def test_health_record_detail_view_url_is_resolved(self):
#         url = reverse('health-record-home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, health_record_detail_view)
#
#     def test_health_record_update_view_url_is_resolved(self):
#         url = reverse('health-record-home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, health_record_update_view)
#
#     def test_health_record_delete_view_url_is_resolved(self):
#         url = reverse('health-record-home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, health_record_delete_view)
#
#
# class TestForms(SimpleTestCase):
#
#     def test_RecordForm_from_valid_data(self):
#         form = RecordForm(data={
#             'title': "test_title",
#             'content': "test_content",
#         })
#         self.assertTrue(form.is_valid())
#
#     def test_RecordForm_form_no_data(self):
#         form = RecordForm(data={})
#
#         self.assertFalse(form.is_valid())
#         self.assertEqual(len(form.errors), 2)
#
#
# class HealthRecordModelTest(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='testuser', password='secret', first_name='fname', last_name='lname',
#             email='testemail@example.com')
#         HealthRecordModel.objects.create(patient=self.user, title='test_title', content='test_content',
#                                          posted_on='2021-08-21')
#
#     def test_content(self):
#         post = HealthRecordModel.objects.get(id=1)
#         expected_object_patient = f'{post.patient}'
#         expected_object_title = f'{post.title}'
#         expected_object_content = f'{post.content}'
#         expected_object_posted_on = f'{post.posted_on}'
#         self.assertEquals(expected_object_patient, self.user.username)
#         self.assertEquals(expected_object_title, 'test_title')
#         self.assertEquals(expected_object_content, 'test_content')
#         self.assertEquals(expected_object_posted_on, '2021-08-21')
#
