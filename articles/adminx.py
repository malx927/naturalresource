# coding=utf-8
import datetime

from xadmin import views
from xadmin.layout import Main, Fieldset, Row, Side

import xadmin
from xadmin.views import LoginView
from .models import *
from django.utils.safestring import mark_safe
from django.db.models import Max


default_form_layout = (
        Main(
            Fieldset('',
                Row("title",),
                Row("sub_title", ),
                Row("source", "doc_url"),
                Row("content"),
                Row("is_publish", "is_top"),
                css_class="unsort short_label no_title",
            ),
        ),
        Side(
            Fieldset(
                "其他信息",
                'abstract', "keywords", "title_image", "show_time", 'hitcounts'
            ),
        )
    )

# 修改登录界面标题
class LoginViewAdmin(LoginView):
    title = settings.SITE_TITLE


xadmin.site.register(LoginView, LoginViewAdmin)


class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseXadminSetting)


class CommXadminSetting(object):
    site_title = settings.SITE_TITLE
    site_footer = settings.SITE_FOOTER

    # def get_site_menu(self):
    #     return (
    #         {'title': '内容管理', 'perm': self.get_model_perm(UserProfile, 'change'), 'menus':(
    #             {'title': '游戏资料', 'icon': 'info-sign', 'url': self.get_model_url(UserProfile, 'changelist') + '?_rel_categories__id__exact=2'},
    #             {'title': '网站文章', 'icon': 'file', 'url': self.get_model_url(UserProfile, 'changelist') + '?_rel_categories__id__exact=1'},
    #         )},
    #     )


xadmin.site.register(views.CommAdminView, CommXadminSetting)


class ChannelAdmin(object):
    """文章栏目"""
    list_display = ['id', 'channel_name', 'parent_channel', 'channel_url', 'channel_image', 'is_singe_page']
    list_display_links = ["channel_name"]
    search_fields = ['channel_name']
    list_per_page = 50
    model_icon = 'fa fa-file-text'


xadmin.site.register(Channel, ChannelAdmin)


class DocumentAdmin(object):
    """文章"""
    list_display = ['id', 'title', 'channel', 'author', 'is_publish', 'is_top', 'show_time', 'create_at', 'hitcounts']
    list_display_links = ('title',)
    exclude = ["author"]
    search_fields = ['title', 'charg_pile.pile_sn', 'name']
    readonly_fields = ["hitcounts"]
    list_filter = ['channel', 'is_publish', 'is_top', 'create_at', 'show_time']
    date_hierarchy = 'show_time'
    list_per_page = 50
    model_icon = 'fa fa-file-text'
    show_all_rel_details = False
    relfield_style = 'fk_select'
    save_on_top = True
    save_as = True
    # style_fields = {
    #     "is_publish": "radio", "is_top": "radio-inline",
    # }

    form_layout = default_form_layout

    # 加载js文件
    def get_media(self):
        media = super(DocumentAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(DocumentAdmin, self).save_models()


# xadmin.site.register(Document, DocumentAdmin)


class NewsAdmin(object):
    """新闻中心"""
    list_display = ['id', 'title', 'channel', 'author', 'is_publish', 'is_top', 'show_time', 'create_at', 'hitcounts']
    list_display_links = ('title',)
    exclude = ["author", "channel"]
    search_fields = ['title']
    readonly_fields = ["hitcounts"]
    list_filter = ['is_publish', 'is_top', 'create_at', 'show_time']
    date_hierarchy = 'show_time'
    list_per_page = 50
    model_icon = 'fa fa-file-text'
    show_all_rel_details = False
    relfield_style = 'fk_select'
    save_on_top = True
    # save_as = True

    form_layout = default_form_layout

    # 加载js文件
    def get_media(self):
        media = super(NewsAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(NewsAdmin, self).save_models()

    def queryset(self):
        qs = super(NewsAdmin, self).queryset().filter(channel__id=4)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(News, NewsAdmin)


class NoticeAdmin(object):
    """公示公告"""
    list_display = ['id', 'title', 'channel', 'author', 'is_publish', 'is_top', 'show_time', 'create_at', 'hitcounts']
    list_display_links = ('title',)
    exclude = ["author", "channel"]
    search_fields = ['title']
    readonly_fields = ["hitcounts"]
    list_filter = ['is_publish', 'is_top', 'create_at', 'show_time']
    date_hierarchy = 'show_time'
    list_per_page = 50
    model_icon = 'fa fa-file-text'
    show_all_rel_details = False
    relfield_style = 'fk_select'
    save_on_top = True
    save_as = True

    form_layout = default_form_layout

    # 加载js文件
    def get_media(self):
        media = super(NoticeAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(NoticeAdmin, self).save_models()

    def queryset(self):
        qs = super(NoticeAdmin, self).queryset().filter(channel__id=5)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Notice, NoticeAdmin)


class InformationAdmin(object):
    """信息发布"""
    list_display = ['id', 'title', 'channel', 'author', 'is_publish', 'is_top', 'show_time', 'create_at', 'hitcounts']
    list_display_links = ('title',)
    exclude = ["author", "channel"]
    search_fields = ['title']
    readonly_fields = ["hitcounts"]
    list_filter = ['is_publish', 'is_top', 'create_at', 'show_time']
    date_hierarchy = 'show_time'
    list_per_page = 50
    model_icon = 'fa fa-file-text'
    show_all_rel_details = False
    relfield_style = 'fk_select'
    save_on_top = True
    save_as = True

    form_layout = default_form_layout

    # 加载js文件
    def get_media(self):
        media = super(InformationAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(InformationAdmin, self).save_models()

    def queryset(self):
        qs = super(InformationAdmin, self).queryset().filter(channel__id=6)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Information, InformationAdmin)


class IndustryNewsAdmin(object):
    """行业动态"""
    list_display = ['id', 'title', 'channel', 'author', 'is_publish', 'is_top', 'show_time', 'create_at', 'hitcounts']
    list_display_links = ('title',)
    exclude = ["author", "channel"]
    search_fields = ['title']
    readonly_fields = ["hitcounts"]
    list_filter = ['is_publish', 'is_top', 'create_at', 'show_time']
    date_hierarchy = 'show_time'
    list_per_page = 50
    model_icon = 'fa fa-file-text'
    show_all_rel_details = False
    relfield_style = 'fk_select'
    save_on_top = True
    save_as = True

    form_layout = default_form_layout

    # 加载js文件
    def get_media(self):
        media = super(IndustryNewsAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(IndustryNewsAdmin, self).save_models()

    def queryset(self):
        qs = super(IndustryNewsAdmin, self).queryset().filter(channel__id=7)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(IndustryNews, IndustryNewsAdmin)


class FriendLinkAdmin(object):
    """友情链接"""
    list_display = ['name', 'link_url', 'link_image', 'create_at']
    search_fields = ['name']


xadmin.site.register(FriendLink, FriendLinkAdmin)


class WebInfoAdmin(object):
    list_display = ['host_unit', 'tech_support', 'address', 'email', 'telephone']


xadmin.site.register(WebInfo, WebInfoAdmin)