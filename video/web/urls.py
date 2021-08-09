#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 17:41
# @Author  : Puxf
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.urls import path

from web import views


app_name = 'web'

urlpatterns = [
    # 主页
    path('', views.index,name='index'),

    # 视频页
    path('video/',views.video,name='video'),

    # 音乐页
    path('music/',views.music,name='music'),

    # 图片页
    path('images1/',views.images,name='images1'),

    # 搜索
    path('search/',views.search,name='search'),

    # 搜索图片
    path('images1/search-images/',views.search_images,name='search_images'),

    # 电视剧
    path('tv-play/',views.tv_play,name='tv-play'),

]
