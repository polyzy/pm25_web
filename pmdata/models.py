#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

#city model
class City(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    points = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = u'城市'

#place model
class Place(models.Model):
    city = models.ForeignKey(City)
    place = models.CharField(max_length=30)

    def __unicode__(self):
        return self.place

    class Meta:
        verbose_name = u'观测点'
        verbose_name_plural = u'观测点'

#grade model
class Grade(models.Model):
    grade = models.CharField(max_length=10)

    def __unicode__(self):
        return self.grade

    class Meta:
        verbose_name = u'评分'
        verbose_name_plural = u'评分'

#pollution model
class Pollution(models.Model):
    pollution = models.CharField(max_length=20)

    def __unicode__(self):
        return self.pollution

    class Meta:
        verbose_name = u'首要污染物'
        verbose_name_plural = u'首要污染物'


#main data model
class Data(models.Model):
    sid = models.ForeignKey(Place)
    AQI = models.IntegerField()
    grade = models.ForeignKey(Grade)
    pollution = models.ForeignKey(Pollution)
    pm25 = models.IntegerField()
    pm10 = models.IntegerField()
    CO = models.FloatField()
    NO2 = models.IntegerField()
    O31 = models.IntegerField()
    O38 = models.IntegerField()
    SO2 = models.IntegerField()
    date = models.BigIntegerField()

    def __unicode__(self):
        return "观测结果%r" % self.grade

    class Meta:
        verbose_name = u'具体观测数据'
        verbose_name_plural = u'具体观测数据'