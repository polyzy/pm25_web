# -*- coding:utf-8 -*-
__author__ = 'andy'

from django import template
register = template.Library()

@register.filter(name='v0')
def v0(m):
    return m.values()[0]

@register.filter(name='k0')
def k0(m):
    return m.keys()[0]
