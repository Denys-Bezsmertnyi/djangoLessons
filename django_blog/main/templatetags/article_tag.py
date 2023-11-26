from django import template
from django.template.defaultfilters import truncatechars

register = template.Library()


@register.inclusion_tag('main/tags_templates/article_template.html')
def display_article(article):
    return {'article': article}
