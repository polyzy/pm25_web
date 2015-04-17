from django.http import HttpResponse
from django.template import loader,RequestContext

from pmdata.models import Data
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request,{
        'name': 'index',
    })
    return HttpResponse(template.render(context))

def index(request):
    template = loader.get_template('index.html')
    pmdatas = Data.objects.all()
    context = RequestContext(request,{
        'pmdatas': pmdatas
    })
    return HttpResponse(template.render(context))