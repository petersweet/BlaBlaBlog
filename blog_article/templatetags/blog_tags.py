from django import template
from ..models import Articles

register = template.Library()


@register.inclusion_tag('blog_article/_article_history.html')
def article_history():
    return {}

def article_history():
    articles = Articles.objects.all()[:5]
    return {'entries': articles}
