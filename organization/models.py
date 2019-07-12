from django.db import models

from articles.models import Document, Channel


class Department(Document):

    class Meta:
        proxy = True
        verbose_name = '内设机构'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel:
            self.channel_id = 2
        return super(Department, self).save(*args, **kwargs)


class DeptDuty(Document):

    class Meta:
        proxy = True
        verbose_name = '主要职责'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel:
            self.channel_id = 3
        return super(DeptDuty, self).save(*args, **kwargs)