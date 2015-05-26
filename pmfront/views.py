from django.http import HttpResponse
from django.template import loader, RequestContext

from pmdata.models import Place, City

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    # pmdatas = Data.objects.all()
    # places = Place.objects.all()
    citys = City.objects.all()
    context = RequestContext(request, {
        'citys': citys
    })
    return HttpResponse(template.render(context))

def detail(request, city_id):
    city = City.objects.get(id=city_id)
    return HttpResponse('City is %s' % (city.name))
