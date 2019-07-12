from django.contrib import admin

import xadmin
from articles.adminx import default_form_layout
from organization.models import Department, DeptDuty


class DepartmentAdmin(object):
    """文章栏目"""
    list_display = ['title', 'author', 'is_publish', 'is_top', 'show_time', 'create_at', 'hitcounts']
    list_display_links = ('title',)
    exclude = ("author", "channel")
    search_fields = ['title']
    readonly_fields = ["hitcounts"]
    list_filter = ['is_publish', 'is_top', 'create_at', 'show_time']
    date_hierarchy = 'show_time'
    list_per_page = 50
    model_icon = 'fa fa-file-text'
    show_all_rel_details = False
    relfield_style = 'fk_select'

    form_layout = default_form_layout

    def queryset(self):
        qs = super(DepartmentAdmin, self).queryset().filter(channel__id=2)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        super(DepartmentAdmin, self).save_models()

    # 加载js文件
    def get_media(self):
        media = super(DepartmentAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media


xadmin.site.register(Department, DepartmentAdmin)


class DeptDutyAdmin(object):
    """文章栏目"""
    list_display = ['title', 'author', 'is_publish', 'is_top', 'show_time', 'create_at', 'hitcounts']
    list_display_links = ('title',)
    exclude = ("author", "channel")
    search_fields = ['title']
    readonly_fields = ["hitcounts"]
    list_filter = ['is_publish', 'is_top', 'create_at', 'show_time']
    date_hierarchy = 'show_time'
    list_per_page = 50
    model_icon = 'fa fa-file-text'
    show_all_rel_details = False
    relfield_style = 'fk_select'

    form_layout = default_form_layout

    def queryset(self):
        qs = super(DeptDutyAdmin, self).queryset().filter(channel__id=3)
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

    def save_models(self):
        obj = self.new_obj
        print(self.request.user)
        obj.author = self.request.user
        super(DeptDutyAdmin, self).save_models()

    # 加载js文件
    def get_media(self):
        media = super(DeptDutyAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            # media.add_js([self.static('civil/js/civilagent.js')])
            media.add_css({"screen": ["articles/css/document.css"]})
        return media

xadmin.site.register(DeptDuty, DeptDutyAdmin)