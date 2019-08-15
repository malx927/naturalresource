from django.conf.urls import url, include
from django.views.generic import TemplateView

from articles.views import IndexListView, NewsDetailView, NewsListView, DocumentListView, SearchListView

urlpatterns = [

   url(r'^article/$', TemplateView.as_view(template_name="articles/base.html"), name='article-index'),
   url(r'^news_detail/(?P<pk>\d+)/$', NewsDetailView.as_view(), name='news-detail'),
   url(r'^newslist/$', NewsListView.as_view(), name='news-list'),
   url(r'^documents/(?P<channelid>\d+)/$', DocumentListView.as_view(), name='document-list'),
   url(r'^search/$', SearchListView.as_view(), name='search-list'),
]