#-*- coding:utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from tasks import fetch_pm_data

pm_recent_task = None


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request,{
        'name':'index',
    })
    return HttpResponse(template.render(context))


def fetch_data(request):
    if request.method == 'POST':
        if pm_recent_task:
            if pm_recent_task.ready():
                return HttpResponse(100)
            else:
                return HttpResponse(0)
        else:
            return HttpResponse(0)
    else:
        #将下面一行注释删除，即可在后台点击调用spider抓取数据，但是要开启Celery服务，使用命令python manage.py celery worker -B，这是开发环境直接使用db作为broker，线上环境不可
        pm_recent_task = fetch_pm_data.delay()
        template = loader.get_template('fetch_running.html')
        context = RequestContext(request,{

        })
        return HttpResponse(template.render(context))