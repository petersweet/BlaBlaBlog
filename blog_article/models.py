from django.db import models

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
