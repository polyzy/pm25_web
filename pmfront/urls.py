__author__ = 'andy'

from django.conf.urls import url,patterns
import views

urlpatterns = patterns('',
    url(r'^detail/(?P<city_id>\d+)/$', views.detail, name='detail'),
)