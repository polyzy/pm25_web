from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import  render_to_response

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
    placeset = city.place_set.all()
    place_and_data = {}
    for p in placeset:
        pd = p.data_set.all()
        if len(pd)>0:
            place_and_data[p] = pd[0]
    model = {
        'city':city,
        'places':place_and_data
    }
    return render_to_response('detail.html',model,context_instance=RequestContext(request))