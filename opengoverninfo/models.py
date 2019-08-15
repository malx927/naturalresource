from django.db import models

from articles.models import Document
from naturalresource import settings


class GovOpenSystem(Document):
    """信息公开制度"""
    class Meta:
        proxy = True
        verbose_name = '信息公开制度'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.channel_id = settings.C_OPEN_SYSTEM
        return super(GovOpenSystem, self).save(*args, **kwargs)


class GovOpenGuide(Document):
    """信息公开指南"""
    class Meta:
        proxy = True
        verbose_name = '信息公开指南'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.channel_id = settings.C_OPEN_GUIDE
        return super(GovOpenGuide, self).save(*args, **kwargs)


class GovOpenList(Document):
    """信息公开目录"""
    class Meta:
        proxy = True
        verbose_name = '信息公开目录'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.channel_id = settings.C_OPEN_LIST
        return super(GovOpenList, self).save(*args, **kwargs)


class GovOpenReport(Document):
    """信息公开年度报告"""
    class Meta:
        proxy = True
        verbose_name = '信息公开年度报告'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.channel_id = settings.C_OPEN_REPORT
        return super(GovOpenReport, self).save(*args, **kwargs)

