from django.contrib import admin

# Register your models here.

from django.contrib import admin
from kombu.transport.django import models as kombu_models
from models import Data,Place,Grade,Pollution

admin.site.register(kombu_models.Message)
admin.site.register(Data)
admin.site.register(Place)
admin.site.register(Grade)
admin.site.register(Pollution)