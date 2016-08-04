# -*- coding: utf-8 -*-
'''
File Name: web/templatetags/tools.py
Author: JackeyGao
mail: gaojunqi@outlook.com
Created Time: 三  7/13 17:17:27 2016
'''
from django import template

register = template.Library()


@register.filter
def g(dt, key):
    if isinstance(dt, dict):
        return dt.get(key, None)
    else:
        return None

@register.filter
def list(string):
    return string.split(',')


