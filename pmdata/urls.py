__author__ = 'andy'
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^fetch/$', views.fetch_data, name='fetch_data'),
)
