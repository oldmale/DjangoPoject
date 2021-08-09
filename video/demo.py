#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 14:15
# @Author  : Puxf
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import hashlib


def hash_code(s,salt='mysite'):
    """密码加密"""
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


passwd = '123456789'

a = hash_code(passwd)




L = ['1','2','3','4','5']
colour = [
        'card bg-primary text-white',
        'card bg-success text-white',
        'card bg-info text-white',
        'card bg-warning text-white',
        'card bg-secondary text-white',

]

for i in colour:
    print(i + '\n')


