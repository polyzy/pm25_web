#-*- coding:utf-8 -*-
#!/usr/bin/python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from twisted.enterprise import adbapi
# from scrapy.http import Request

#直接使用scrapy将爬到的数据用django的orm保存到对应实体的表中
#如果单独运行scrapy,需要设置环境变量export DJANGO_SETTINGS_MODULE=pm25_web.settings
#

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.pardir)))

from pmdata.models import Data, City, Place,Pollution,Grade
from pypinyin import lazy_pinyin

import django
django.setup()


class Pm25SpiderPipeline(object):
    # def __init__(self):
    #     dbpath = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.pardir)),
    #                           'db.sqlite3')
    #     self.conn = sqlite3.connect(dbpath)
    #     self.cursor = self.conn.cursor()
    #     self.cursor.execute(
    #         'CREATE TABLE if not exists testdata(city varchar,place varchar,AQI varchar,grade varchar,pollution varchar,pm25 varchar,pm10 varchar,CO varchar,NO2 varchar,O31 varchar,O38 varchar,SO2 varchar,dt varchar)');
    #

    def process_item(self, item, spider):
        city_name = item['city']
        place_name = item['place']
        grade_name = item['grade']
        pollution_name = item['pollution']
        if City.objects.filter(name=city_name).count()>0:
            city = City.objects.filter(name=city_name)[0]
        else:
            city = City(name=city_name,code=''.join(lazy_pinyin(city_name)))
            city.save()
        if Place.objects.filter(place=place_name).count()>0:
            place = Place.objects.filter(place=place_name)[0]
        else:
            place = Place(city=city,place=place_name)
            place.save()
        if Grade.objects.filter(grade=grade_name).count()>0:
            grade = Grade.objects.filter(grade=grade_name)[0]
        else:
            grade = Grade(grade=grade_name)
            grade.save()
        if Pollution.objects.filter(pollution=pollution_name).count()>0:
            pollution = Pollution.objects.filter(pollution=pollution_name)[0]
        else:
            pollution = Pollution(pollution=pollution_name)
            pollution.save()
        print 'got one record.'
        # self.cursor.execute(
        #     'insert into testdata (city,place,AQI,grade,pollution,pm25,pm10,CO,NO2,O31,O38,SO2,dt) values ("%s","%s",%s,"%s","%s",%s,%s,%s,%s,%s,%s,%s,%s); ' % (
        #     item['city'], item['place'], item['AQI'], item['grade'], item['pollution'], item['pm25'], item['pm10'],
        #     item['CO'], item['NO2'], item['O31'], item['O38'], item['SO2'], item['date']))
        # self.conn.commit()
        data = Data(sid=place,grade=grade,AQI=int(item['AQI']),pollution=pollution,pm25=item['pm25'],pm10=item['pm10'],CO=item['CO'],NO2=item['NO2'],O31=item['O31'],O38=item['O38'],SO2=item['SO2'],date=item['date'])
        data.save()
