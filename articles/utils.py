# coding=utf-8
from collections import  OrderedDict
from django.urls import reverse
from .models import Channel


def get_breadcrumbs(channelid):
    """获取栏目导航路径"""
    breadcrumb = OrderedDict()
    try:
        ch = Channel.objects.get(id=channelid)
        ch_url = reverse("document-list", kwargs={"channelid": ch.id})
        breadcrumb[ch.channel_name] = ch_url
        while(ch.parent_channel):
            ch = Channel.objects.get(id=ch.parent_channel.id)
            ch_url = reverse("document-list", kwargs={"channelid": ch.id})
            breadcrumb[ch.channel_name] = ch_url
    except Channel.DoesNotExist as ex:
        return None

    breadcrumb["首页"] = "/"
    crumbs = OrderedDict()
    for k, v in reversed(breadcrumb.items()):
        crumbs[k] = v
    return crumbs