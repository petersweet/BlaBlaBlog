from django.template import Context, Template
from django.test import TestCase
from .models import Articles
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import CommentForm

# Create your tests here.

class ModelTesting(TestCase):



    def setUp(self):
        self.article_title = "World class code"
        self.some_user = User.objects.create(username="nerd")
        self.article = Articles(title=self.article_title, author=self.some_user)
        self.comment = Comment (body = self.article_title)

    def string_representation(self):
        self.assertEqual(str(self.article), self.article.title)
        self.assertEqual(str(self.comment), self.article_title)


    def test_model_create_article(self):
        old_count = Articles.objects.count()
        self.article.save()
        new_count = Articles.objects.count()
        self.assertNotEqual(old_count, new_count)

class CommentFormTest(TestCase):

    def setUp(self):
        self.article_title = "World class code"
        self.some_user = get_user_model().objects.create(username="nerd")
        self.article = Articles(title=self.article_title, author=self.some_user)

    def test_init(self):
        CommentForm(article=self.article)

    def test_init_without_entry(self):
        with self.assertRaises(KeyError):
            CommentForm()

    def test_valid_data(self):
        form = CommentForm({
            'name': "Peter Sweet",
            'email': "Grynevich@example.com",
            'body': "Hi there",
        }, article=self.article)
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.name, "Peter Sweet")
        self.assertEqual(comment.email, "Grynevich@example.com")
        self.assertEqual(comment.body, "Hi there")
        self.assertEqual(comment.entry, self.article)

    def test_blank_data(self):
        form = CommentForm({}, article=self.article)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'email': ['Thi[55 chars]d.'],
            'body': ['required'],
        })

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


class EntryHistoryTagTest(TestCase):

    TEMPLATE = Template("{% load blog_tags %} {% article_history %}")

    def setUp(self):
        self.user = get_user_model().objects.create(username='nerd')

    def test_entry_shows_up(self):
        article = Articles.objects.create(author=self.user, title="My entry title")
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn(article.title, rendered)

    def test_no_posts(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn("No recent articles", rendered)

    def test_many_posts(self):
        for n in range(6):
            Articles.objects.create(author=self.user, title="Post #{0}".format(n))
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn("Post #5", rendered)
        self.assertNotIn("Post #6", rendered)