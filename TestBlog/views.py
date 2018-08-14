from django.views.generic import ListView
from blog_article.models import Articles
from django.shortcuts import render

# Create your views here.

class HomeView(ListView):
    template_name = 'index.html'
    queryset = Articles.objects.order_by('-date_created')


