
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.ArticleList.as_view()),
    url(r'^<int:pk>/', views.ArticleDetail.as_view()),
]
