"""naturalresource URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

import xadmin
from articles.views import IndexListView
from naturalresource import settings
from django.conf.urls.static import static
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', IndexListView.as_view(), name='site-index'),
    url(r'^xadmin/2019/', xadmin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^article/', include('articles.urls')),
    url(r'^organization/', include('organization.urls')),
    url(r'^ogi/', include('opengoverninfo.urls')),
    url(r'^fanancial/', include('fanancial.urls')),
    url(r'^notice/$', TemplateView.as_view(template_name="articles/base.html"), name='notice-index'),
    url(r'^info/$', TemplateView.as_view(template_name="articles/base.html"), name='information-index'),
    url(r'^industnews/$', TemplateView.as_view(template_name="articles/base.html"), name='industry-news-index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
