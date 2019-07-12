from django.contrib import admin

import xadmin
from articles.adminx import default_form_layout
from fanancial.models import FananBudget, FananAccount


class FananBudgetAdmin(object):
    """部门预算"""
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
        media = super(FananBudgetAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(FananBudgetAdmin, self).save_models()

    def queryset(self):
        qs = super(FananBudgetAdmin, self).queryset().filter(channel__id=14)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(FananBudget, FananBudgetAdmin)


class FananAccountAdmin(object):
    """部门决算"""
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
        media = super(FananAccountAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(FananAccountAdmin, self).save_models()

    def queryset(self):
        qs = super(FananAccountAdmin, self).queryset().filter(channel__id=15)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(FananAccount, FananAccountAdmin)