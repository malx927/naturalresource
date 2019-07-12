from django.conf.urls import url, include
from django.views.generic import TemplateView


urlpatterns = [
   # url(r'^$', ArticleListView.as_view(), name='article-index'),
   url(r'^$', TemplateView.as_view(template_name="articles/base.html"), name='fanancial-index'),
]