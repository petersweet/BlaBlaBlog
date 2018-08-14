from django.test import TestCase
from .models import Articles
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your tests here.

class ModelTesting(TestCase):



    def setUp(self):
        self.article_title = "World class code"
        self.some_user = User.objects.create(username="nerd")
        self.article = Articles(title=self.article_title, author=self.some_user)

    def string_representation(self):
        self.assertEqual(str(self.article), self.article.title)

    def test_model_create_article(self):
        old_count = Articles.objects.count()
        self.article.save()
        new_count = Articles.objects.count()
        self.assertNotEqual(old_count, new_count)


class HomePageTesting(TestCase):

    def setUp(self):
        self.title_1 = "1-title"
        self.title_2 = "2-title"
        self.body_1 = "1-body"
        self.body_2 = "2-body"
        self.user = get_user_model().objects.create(username="nerd")
        self.response_start_page = self.client.get('/')


    def test_start_page(self):
        self.assertEqual(self.response_start_page.status_code, 200)



    def test_one_entry(self):
        Articles.objects.create(title=self.title_1, body=self.body_1, author=self.user)
        self.assertContains(self.response_start_page, self.title_1)
        self.assertContains(self.response_start_page, self.body_1)

    def test_two_entries(self):
        Articles.objects.create(title=self.title_1, body=self.body_1, author=self.user)
        Articles.objects.create(title=self.title_1, body=self.body_2, author=self.user)
        self.assertContains(self.response_start_page, self.title_1)
        self.assertContains(self.response_start_page, self.body_1)
        self.assertContains(self.response_start_page, self.title_2)
        self.assertContains(self.response_start_page, self.body_2)

    def test_no_entries(self):
        self.assertContains(self.response_start_page, 'No blog entries yet.')

class EntryViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username="nerd")
        self.article = Articles.objects.create(title='1-title', body='1-body', author=self.user)
        self.response_entry = self.client.get(self.article.get_absolute_url())

    def test_basic_view(self):
        self.assertEqual(self.response_entry.status_code, 200)

    def test_get_absolute_url(self):
        self.assertIsNotNone(self.article.get_absolute_url())