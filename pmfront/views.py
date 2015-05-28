from django.http import HttpResponse
from django.template import loader, RequestContext

from pmdata.models import Place, City

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    # pmdatas = Data.objects.all()
    # places = Place.objects.all()
    hot_cities = City.objects.order_by('-points')[0:5]
    city_with_dict = []
    for i in range(65,65+26):
        k = chr(i)
        k_citys = City.objects.filter(code__istartswith=k)
        if k_citys:
            city_with_dict.append({k:k_citys})
    context = RequestContext(request, {
        'hot_cities':hot_cities,
        'citys': city_with_dict
    })
    return HttpResponse(template.render(context))

def detail(request, city_id):
    city = City.objects.get(id=city_id)
    return HttpResponse('City is %s' % (city.name))
