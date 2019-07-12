# coding=utf-8
import datetime

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext as _
from xadmin.layout import Main, Fieldset, Row, Side

import xadmin
from xadmin.plugins.auth import PermissionModelMultipleChoiceField
from .models import *
from django.utils.safestring import mark_safe
from django.db.models import Max


class UserInfoAdmin(object):
    change_user_password_template = None
    list_display = ('username', 'first_name', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name',)
    ordering = ('username',)
    style_fields = {'user_permissions': 'm2m_transfer'}
    model_icon = 'fa fa-user'
    relfield_style = 'fk-select'

    def get_field_attrs(self, db_field, **kwargs):
        attrs = super(UserInfoAdmin, self).get_field_attrs(db_field, **kwargs)
        if db_field.name == 'user_permissions':
            attrs['form_class'] = PermissionModelMultipleChoiceField
        return attrs

    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = UserCreationForm
        else:
            self.form = UserChangeForm
        return super(UserInfoAdmin, self).get_model_form(**kwargs)

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             Row('email', None),
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserInfoAdmin, self).get_form_layout()


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserInfoAdmin)