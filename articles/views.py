from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.db.models.query import EmptyQuerySet
from django.shortcuts import render

from django.views import View
from django.views.generic import DetailView

from articles.models import Document, FriendLink, Channel
from articles.utils import get_breadcrumbs
from naturalresource import settings


class IndexListView(View):
    """首页"""
    def get(self, request, *args, **kwargs):
        # 首页轮播(新闻中心)
        image_news = Document.objects.filter(channel=4, title_image__isnull=False, is_publish=1)[0:5]
        news = Document.objects.filter(channel=4, is_publish=1)[0:9]
        notices = Document.objects.filter(channel=5,  is_publish=1)[0:6]
        informations = Document.objects.filter(channel=6,  is_publish=1)[0:6]
        industry_news = Document.objects.filter(channel=7,  is_publish=1)[0:6]
        ogis = Document.objects.filter(channel__parent_channel_id=8,  is_publish=1)[0:6]
        links = FriendLink.objects.all()
        budgets = Document.objects.filter(channel=14,  is_publish=1)
        accounts = Document.objects.filter(channel=15,  is_publish=1)
        site_name = settings.SITE_FOOTER

        context = {
            "image_news": image_news,
            "news": news,
            "notices": notices,
            "informations": informations,
            "industry_news": industry_news,
            "ogis": ogis,
            "links": links,
            "budgets": budgets,
            "accounts": accounts,
            "site_name": site_name,
        }

        return render(request, template_name="articles/index.html", context=context)


class NewsDetailView(DetailView):
    """新闻详细页"""
    model = Document
    template_name = 'articles/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = settings.SITE_FOOTER
        channelid = self.object.channel.id
        context["breadcrumbs"] = get_breadcrumbs(channelid)
        return context

    def get(self, request, *args, **kwargs):
        response = super(NewsDetailView, self).get(request, *args, **kwargs)
        self.object.hitcounts += 1
        self.object.save()
        return response


class NewsListView(View):
    """新闻中心列表"""
    def get(self, request, *args, **kwargs):
        return render(request, template_name="articles/detail.html")


class DocumentListView(View):
    """文章列表"""
    def get(self, request, *args, **kwargs):
        channelid = kwargs.get("channelid", None)
        page = int(request.GET.get("page", 1))
        context = {}
        context["site_name"] = settings.SITE_FOOTER
        if channelid:
            context["channelid"] = int(channelid)
            try:
                channel = Channel.objects.get(id=channelid)
                context["channel_name"] = channel.channel_name
                channel_path = get_breadcrumbs(channelid)
                context["breadcrumbs"] = channel_path
                channels = channel.get_children()
                if channels and len(channels) > 0:
                    context["channels"] = channels
                else:
                    parent_channels = channel.get_parent_children()

                    if parent_channels and len(parent_channels) > 0:
                        context["channels"] = parent_channels
                    else:
                        context["channels"] = Channel.objects.filter(id=channelid)

                if channel.is_singe_page == 1:          # 单页
                    single = Document.objects.filter(channel=channelid, is_publish=1).first()
                    print(single, 'single')
                    context["single"] = single
                    return  render(request, template_name="articles/single.html", context=context)
                else:
                    documents = Document.objects.filter(Q(channel=channelid)|Q(channel__parent_channel=channelid), is_publish=1)
                    paginator = Paginator(documents, settings.PAGE_SIZE)

                    context["num_pages"] = paginator.num_pages
                    context["count"] = paginator.count

                    try:
                        page_obj = paginator.page(page)
                    except PageNotAnInteger:
                        page_obj = paginator.page(1)
                    except EmptyPage:
                        page_obj = paginator.page(paginator.num_pages)

                    context["page"] = page_obj
            except Channel.DoesNotExist as ex:
                return render(request, template_name="articles/list.html", context=context)

        return render(request, template_name="articles/list.html", context=context)


class SearchListView(View):
    """搜索"""
    def get(self, request, *args, **kwargs):
        q = request.GET.get("q", None)
        page = int(request.GET.get("page", 1))
        context = {}
        context["site_name"] = settings.SITE_FOOTER
        print(q)
        if q:
            documents = Document.objects.filter(title__contains=q)
            paginator = Paginator(documents, settings.PAGE_SIZE)

            context["num_pages"] = paginator.num_pages
            context["count"] = paginator.count

            try:
                page_obj = paginator.page(page)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            context["page"] = page_obj
        else:
            context["page"] = None

        return render(request, template_name="articles/search_list.html", context=context)
