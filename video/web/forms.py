#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 15:42
# @Author  : Puxf
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from django import forms

class SearchForm(forms.Form):
    """搜索表单"""
    search = forms.CharField(label='搜索',max_length=256,
                             widget=forms.TextInput(attrs={'class': 'form-search','placeholder':"中国医生"}))
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "用户名"}))

