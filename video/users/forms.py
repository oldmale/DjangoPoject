#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 10:46
# @Author  : Puxf
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"用户名"}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':"密码"}))



class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"用户名"}))
    password1 = forms.CharField(label="密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':"密码"}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':"确认密码"}))
    email = forms.EmailField(label="邮箱地址",
                             widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':"电子邮箱"}))