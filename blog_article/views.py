from django.shortcuts import render
from django.views.generic import DetailView
from blog_article.models import Articles
# Create your views here.

class ArticlesDetail(DetailView):
    model = Articles