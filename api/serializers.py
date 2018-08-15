from rest_framework import serializers
from blog_article.models import Articles


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articles
        fields = ('id',
                  'title',
                  'body',
                  'slug',
                  'author',
                  'date_created',
                  'date_modified')

        read_only_fields = ('date_created',
                            'date_modified')
        