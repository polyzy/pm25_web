#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, RequestContext
from django.shortcuts import  render_to_response

from pmdata.models import Place, City

import time,datetime

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
    city = City.objects.safe_get(id=city_id)
    if not city:
        return HttpResponseBadRequest("非法参数")
    city.points = city.points+1
    city.save()
    placeset = city.place_set.all()
    place_and_data = {}
    tnow = datetime.datetime.now()
    t0 = time.mktime((tnow.year,tnow.month,tnow.day,0,0,0,0,0,0))
    for p in placeset:
        pd = p.data_set.filter(date__gt=t0).all()
        if len(pd)>0:
            place_and_data[p] = pd[0]
    model = {
        'city':city,
        'places':place_and_data
    }
    return render_to_response('detail.html',model,context_instance=RequestContext(request))

def fresh(request):
    pass
