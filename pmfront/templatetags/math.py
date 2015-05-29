#-*- coding:utf-8 -*-
__author__ = 'andy'

"""
    自定义模板filter，实现简单算术运算
"""

from django import template
register = template.Library()

@register.filter(name='add')
def add(value,n2):
    return value+n2

@register.filter(name='minus')
def minus(value,n2):
    return value-n2

@register.filter(name='multiply')
def minus(value,n2):
    return value*n2