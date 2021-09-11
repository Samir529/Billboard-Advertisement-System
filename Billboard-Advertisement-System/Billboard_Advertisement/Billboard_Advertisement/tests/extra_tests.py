#
#
# class UserTest(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='testuser', password='secret', first_name='Samir', last_name='Asif', email='testemail@example.com')
#
#     def test_content(self):
#         user = User.objects.get(id=1)
#         expected_object_username = f'{user.username}'
#         # expected_object_password = f'{user.password}'
#         expected_object_first_name = f'{user.first_name}'
#         expected_object_last_name = f'{user.last_name}'
#         expected_object_email = f'{user.email}'
#         self.assertEquals(expected_object_username, 'testuser')
#         # self.assertEquals(expected_object_password, 'secret')
#         self.assertEquals(self.user.check_password('secret'), True)
#         self.assertEquals(expected_object_first_name, 'Samir')
#         self.assertEquals(expected_object_last_name, 'Asif')
#         self.assertEquals(expected_object_email, 'testemail@example.com')
#
#     def test_user_label(self):
#         user = User.objects.get(id=1)
#         field_label = user._meta.get_field('username').verbose_name
#         self.assertEqual(field_label, 'username')
#
#     def test_object_name_is_username(self):
#         user = User.objects.get(id=1)
#         expected_object_name = f'{user.username}'
#         self.assertEqual(str(user), expected_object_name)
#
#
#
#     def test_is_advertiser_label(self):
#         user = AdvertiserProfileInfo.objects.get(id=1)
#         field_label = user._meta.get_field('is_advertiser').verbose_name
#         self.assertEqual(field_label, 'is advertiser')
#
#     def test_mobileNo_max_length(self):
#         user = AdvertiserProfileInfo.objects.get(id=1)
#         max_length = user._meta.get_field('mobileNo').max_length
#         self.assertEqual(max_length, 14)
#
#     def test_object_name_is_user(self):
#         user = AdvertiserProfileInfo.objects.get(id=1)
#         expected_object_name = f'{user.user}'
#         self.assertEqual(str(user), expected_object_name)
#
#
#
#     def test_is_cityCor_label(self):
#         user = CityCorporationProfileInfo.objects.get(id=1)
#         field_label = user._meta.get_field('is_cityCor').verbose_name
#         self.assertEqual(field_label, 'is cityCor')
#
#     def test_mobileNo_max_length(self):
#         user = CityCorporationProfileInfo.objects.get(id=1)
#         max_length = user._meta.get_field('mobileNo').max_length
#         self.assertEqual(max_length, 14)
#
#     def test_object_name_is_user(self):
#         user = CityCorporationProfileInfo.objects.get(id=1)
#         expected_object_name = f'{user.user}'
#         self.assertEqual(str(user), expected_object_name)





















