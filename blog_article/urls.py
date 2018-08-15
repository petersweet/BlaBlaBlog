from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<pk>\d+)-(?P<slug>[-\w]*)/$',
        views.ArticlesDetail.as_view(), name='article_detail'),
]