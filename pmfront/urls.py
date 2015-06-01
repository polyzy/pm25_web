__author__ = 'andy'

from django.conf.urls import url,patterns
from simple_views import AboutView,SponserView
import views

urlpatterns = patterns('',
    url(r'^detail/(?P<city_id>\d+)/$', views.detail, name='detail'),
    url(r'^detail/fresh/$', views.fresh, name='fresh'),
    url(r'^about/$',AboutView.as_view(),name='about'),
    url(r'^sponser/$',SponserView.as_view(),name='sponser'),
)