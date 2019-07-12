from django.contrib import admin

import xadmin
from articles.adminx import default_form_layout
from opengoverninfo.models import GovOpenSystem, GovOpenGuide, GovOpenList, GovOpenReport


class GovOpenSystemAdmin(object):
    """信息公开制度"""
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
        media = super(GovOpenSystemAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(GovOpenSystemAdmin, self).save_models()

    def queryset(self):
        qs = super(GovOpenSystemAdmin, self).queryset().filter(channel__id=9)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(GovOpenSystem, GovOpenSystemAdmin)


class GovOpenGuideAdmin(object):
    """信息公开指南"""
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
        media = super(GovOpenGuideAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(GovOpenGuideAdmin, self).save_models()

    def queryset(self):
        qs = super(GovOpenGuideAdmin, self).queryset().filter(channel__id=9)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(GovOpenGuide, GovOpenGuideAdmin)


class GovOpenListAdmin(object):
    """信息公开指南"""
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
        media = super(GovOpenListAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(GovOpenListAdmin, self).save_models()

    def queryset(self):
        qs = super(GovOpenListAdmin, self).queryset().filter(channel__id=10)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(GovOpenList, GovOpenListAdmin)


class GovOpenReportAdmin(object):
    """信息公开年度报告"""
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
        media = super(GovOpenReportAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(GovOpenReportAdmin, self).save_models()

    def queryset(self):
        qs = super(GovOpenReportAdmin, self).queryset().filter(channel__id=10)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(GovOpenReport, GovOpenReportAdmin)