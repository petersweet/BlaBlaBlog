from django.shortcuts import render
from django.views.generic import DetailView
from blog_article.models import Articles
# Create your views here.

class ArticlesDetail(DetailView):
    model = Articles

    def get_success_url(self):
        return self.get_object().get_absolute_url()