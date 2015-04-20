# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from tasks import fetch_pm_data


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request,{
        'name':'index',
    })
    return HttpResponse(template.render(context))


def fetch_data(request):
    fetch_pm_data.delay()
    template = loader.get_template('fetch_running.html')
    context = RequestContext(request,{

    })
    return HttpResponse(template.render(context))