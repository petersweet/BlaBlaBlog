from django.db import models
from django.urls import reverse



# Create your models here.

class Articles (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        related_name='article',
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "{}".format(self.title, self.body, self.date_created, self.date_modified)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    article = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "{}".format(self.article, self.name, self.date_created, self.date_modified, self.body)

