from django.contrib import admin

# Register your models here.

from django.contrib import admin
from kombu.transport.django import models as kombu_models
from models import Data, Place, Grade, Pollution, City


class DataAdmin(admin.ModelAdmin):
    list_display = ('sid', 'AQI', 'grade', 'pollution', 'pm25', 'pm10', 'CO', 'NO2', 'O31', 'O38', 'SO2')


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('city', 'place')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade',)


class PollutionAdmin(admin.ModelAdmin):
    list_display = ('pollution',)





class CityAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


admin.site.register(kombu_models.Message)
admin.site.register(Data, DataAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Pollution, PollutionAdmin)
admin.site.register(City, CityAdmin)