# class TestUrls(SimpleTestCase):
#
#     def test_advisor_post_create_view_url_is_resolved(self):
#         url = reverse('advisor-post-create')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, advisor_post_create_view)
#
#     def test_advisor_home_view_url_is_resolved(self):
#         url = reverse('advisor-home')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, advisor_home_view)
#
#     def test_advisor_post_detail_view_url_is_resolved(self):
#         url = reverse('advisor-post-detail')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, advisor_post_detail_view)
#
#     def test_advisor_post_update_view_url_is_resolved(self):
#         url = reverse('advisor-post-update')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, advisor_post_update_view)
#
#     def test_advisor_post_delete_view_url_is_resolved(self):
#         url = reverse('advisor-post-delete')
#         print(resolve(url))
#         self.assertEquals(resolve(url).func, advisor_post_delete_view)
#
#
# class TestForms(SimpleTestCase):
#
#     def test_AddEditPostForm_from_valid_data(self):
#         form = AddEditPostForm(data={
#             'title': "test_title",
#             'content': "test_content",
#             'image': "/posted_billboards_pic/billboards_images/demo_billboard_image.JPG",
#         })
#         self.assertTrue(form.is_valid())
#
#     def test_AddEditPostForm_form_no_data(self):
#         form = AddEditPostForm(data={})
#
#         self.assertFalse(form.is_valid())
#         self.assertEqual(len(form.errors), 3)
#
#
# class AdviceModelTest(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='testuser', password='secret', first_name='fname', last_name='lname',
#             email='testemail@example.com')
#         AdviceModel.objects.create(author=self.user, title='test_title', content='test_content',
#                                    image='/posted_billboards_pic/billboards_images/sample_image.JPG',
#                                    date_posted='2021-08-21', slug='aa', totalViewCount=3)
#
#     def test_content(self):
#         post = AdviceModel.objects.get(id=1)
#         expected_object_author = f'{post.author}'
#         expected_object_title = f'{post.title}'
#         expected_object_content = f'{post.content}'
#         expected_object_image = f'{post.posted_billboards_pic}'
#         expected_object_date_posted = f'{post.date_posted}'
#         expected_object_slug = f'{post.slug}'
#         expected_object_totalViewCount = f'{post.totalViewCount}'
#         self.assertEquals(expected_object_author, self.user.username)
#         self.assertEquals(expected_object_title, 'test_title')
#         self.assertEquals(expected_object_content, 'test_content')
#         self.assertEquals(expected_object_image, '/posted_billboards_pic/billboards_images/sample_image.JPG')
#         self.assertEquals(expected_object_date_posted, '2021-08-21')
#         self.assertEquals(expected_object_slug, 'aa')
#         self.assertEquals(expected_object_totalViewCount, '3')
#
#
#
#
#
#
#
#
#
#
