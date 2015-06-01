# -*- coding:utf-8 -*-
__author__ = 'andy'

from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = 'about.html'

class SponserView(TemplateView):
    template_name = 'sponser.html'
