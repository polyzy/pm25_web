from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pm25_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','pmfront.views.index'),
    url(r'^pmdata/',include('pmdata.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
