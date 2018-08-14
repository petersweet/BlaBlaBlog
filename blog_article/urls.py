from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ArticlesDetail.as_view(), name='article_detail'),
]