from django.shortcuts import render
from rest_framework import generics

from blog_article.models import Articles
from .serializers import ArticleSerializer
# Create your views here.

class ArticleList(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
