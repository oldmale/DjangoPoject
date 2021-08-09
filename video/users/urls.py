#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 09:22
# @Author  : Puxf
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.contrib import admin
from django.urls import path,include

from users import views

app_name = 'users'

urlpatterns = [

    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout')
]