#!/usr/bin/python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
# from twisted.enterprise import adbapi
# from scrapy.http import Request
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import  MySQLdb
import MySQLdb.cursors

import sqlite3

class Pm25SpiderPipeline(object):
      def __init__(self):
            self.conn = sqlite3.connect('db.sqlite3')
	    self.cursor = self.conn.cursor()
	    self.cursor.execute('CREATE TABLE if not exists testdata(city varchar,place varchar,AQI varchar,grade varchar,pollution varchar,pm25 varchar,pm10 varchar,CO varchar,NO2 varchar,O31 varchar,O38 varchar,SO2 varchar,dt varchar)');
	    

      def process_item(self, item, spider):
            print item['AQI'],item['grade'],item['pollution'],item['pm25'],item['pm10'],item['CO'],item['NO2'],item['O31'],item['O38'],item['SO2'],item['date'] 
            self.cursor.execute('insert into testdata (city,place,AQI,grade,pollution,pm25,pm10,CO,NO2,O31,O38,SO2,dt) values ("%s","%s",%s,"%s","%s",%s,%s,%s,%s,%s,%s,%s,%s); '%(item['city'],item['place'],item['AQI'],item['grade'],item['pollution'],item['pm25'],item['pm10'],item['CO'],item['NO2'],item['O31'],item['O38'],item['SO2'],item['date']))
            self.conn.commit()
            return item
