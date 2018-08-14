from django.test import TestCase
from .models import Articles
from django.contrib.auth.models import User

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

class MapingTesting(TestCase):

    def setUp(self):
        self.response_start_page = self.client.get('/')


    def test_start_page(self):
        self.assertEqual(self.response_start_page.status_code, 200)