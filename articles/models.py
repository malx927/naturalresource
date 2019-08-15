import datetime

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from naturalresource import settings


class Channel(models.Model):
    """文章栏目"""
    SINGE_PAGE = (
        (0, '否'),
        (1, '单页'),
    )
    channel_name = models.CharField(verbose_name="栏目", max_length=64)
    parent_channel = models.ForeignKey('self', verbose_name='父栏目', blank=True, null=True)
    channel_image = models.ImageField(verbose_name='栏目LOGO', upload_to="channel/", blank=True, null=True)
    channel_url = models.URLField(verbose_name='栏目链接', max_length=600, blank=True, null=True)
    is_singe_page = models.IntegerField(verbose_name="是否是单页", choices=SINGE_PAGE, default=0)
    update_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    create_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.channel_name

    class Meta:
        verbose_name = '栏目维护'
        verbose_name_plural = verbose_name
        ordering = ["create_at"]

    def get_children(self):
        return self.channel_set.all()

    def get_parent_children(self):
        if self.parent_channel:
            return Channel.objects.filter(parent_channel=self.parent_channel)
        else:
            return None


class Document(models.Model):
    """新闻中心"""
    title = models.CharField(verbose_name='标题', max_length=500)
    channel = models.ForeignKey(Channel, verbose_name="栏目", on_delete=models.SET_NULL, null=True, blank=True)
    sub_title = models.CharField(verbose_name='副标题', max_length=500, blank=True, null=True)
    title_image = models.ImageField(verbose_name='标题图片', upload_to="articles/", blank=True, null=True)
    source = models.CharField(verbose_name="来源", max_length=64, blank=True, null=True)
    doc_url = models.URLField(verbose_name='链接地址', max_length=500, blank=True, null=True)
    content = RichTextUploadingField(verbose_name='文章内容', blank=True, null=True)
    abstract = models.TextField(verbose_name='摘要', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', null=True, blank=True, on_delete=models.SET_NULL)
    keywords = models.CharField(verbose_name='关键词', max_length=200, blank=True, null=True)
    is_publish = models.IntegerField(verbose_name='是否发布', choices=((0, '草稿'), (1, '发布')), default=1)
    is_top = models.IntegerField(verbose_name='是否置顶', choices=((0, '否'), (1, '置顶')), default=0)
    show_time = models.DateTimeField(verbose_name="显示时间", default=datetime.datetime.now)
    update_at = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    hitcounts = models.IntegerField(verbose_name='点击次数', blank=True, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻中心'
        verbose_name_plural = verbose_name
        ordering = ["-show_time"]

    def save(self, *args, **kwargs):

        if not self.channel_id:
            self.channel_id = settings.C_NEWS
        return super(Document, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"pk": self.id})

    # 下一篇
    def next_article(self):
        return Document.objects.filter(show_time__gt=self.show_time, channel=self.channel).order_by('show_time').first()

    # 上一篇
    def pre_article(self):
        return Document.objects.filter(show_time__lt=self.show_time, channel=self.channel).order_by('-show_time').first()

    def channel_name(self):
        if self.channel:
            return self.channel.channel_name
        return ""


# class News(Document):
#
#     class Meta:
#         proxy = True
#         verbose_name = '新闻中心'
#         verbose_name_plural = verbose_name
#
#     def save(self, *args, **kwargs):
#         if not self.channel:
#             self.channel_id = 4
#         return super(News, self).save(*args, **kwargs)
#
#     def get_absolute_url(self):
#         return reverse("news-detail", kwargs={"pk": self.id})


class Notice(Document):

    class Meta:
        proxy = True
        verbose_name = '告示公告'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.channel_id = settings.C_NOTICE
        return super(Notice, self).save(*args, **kwargs)


class Information(Document):

    class Meta:
        proxy = True
        verbose_name = '信息发布'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel_id:
            self.channel_id = settings.C_INFO
        return super(Information, self).save(*args, **kwargs)


class IndustryNews(Document):

    class Meta:
        proxy = True
        verbose_name = '行业动态'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.channel:
            self.channel_id = settings.C_INDUSTRY
        return super(IndustryNews, self).save(*args, **kwargs)


class FriendLink(models.Model):
    """友情链接"""
    name = models.CharField(verbose_name='名称', max_length=64)
    link_url = models.URLField(verbose_name='链接地址', max_length=600)
    link_image = models.ImageField(verbose_name='链接图片', blank=True, null=True)
    sort = models.IntegerField(verbose_name='排序', default=0)
    create_at = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ["sort", "create_at"]


class WebInfo(models.Model):
    host_unit = models.CharField(verbose_name="主办单位", max_length=100, blank=True, null=True)
    tech_support = models.CharField(verbose_name="技术支持", max_length=100, blank=True, null=True)
    address = models.CharField(verbose_name="地址", max_length=120, blank=True, null=True)
    email = models.EmailField(verbose_name="邮箱", max_length=50, blank=True, null=True)
    post_code = models.CharField(verbose_name="邮编", max_length=30, blank=True, null=True)
    telephone = models.CharField(verbose_name="电话", max_length=30, blank=True, null=True)
    record_no = models.CharField(verbose_name='辽ICP备', max_length=50, blank=True, null=True)
    police_no = models.CharField(verbose_name='辽公网安备', max_length=50, blank=True, null=True)
    web_code = models.CharField(verbose_name='网站标识码', max_length=50, blank=True, null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now=True)

    def __str__(self):
        return self.host_unit

    class Meta:
        verbose_name = "网站信息"
        verbose_name_plural = verbose_name