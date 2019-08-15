from django.db import models

from articles.models import Document
from naturalresource import settings


class FananBudget(Document):
    """部门预算"""
    class Meta:
        proxy = True
        verbose_name = '部门预算'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.channel_id = settings.C_BUDGETS
        return super(FananBudget, self).save(*args, **kwargs)


class FananAccount(Document):
    """部门决算"""
    class Meta:
        proxy = True
        verbose_name = '部门决算'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.channel_id = settings.C_ACCOUNTS
        return super(FananAccount, self).save(*args, **kwargs)