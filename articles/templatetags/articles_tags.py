from django import template

from articles.models import WebInfo

register = template.Library()


@register.simple_tag
def web_info():
    return WebInfo.objects.all().first()