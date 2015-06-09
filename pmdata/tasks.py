__author__ = 'andy'


from celery import task
import os

pm_spider_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)),'pm25')

@task
def fetch_pm_data():
    print 'fetch data by python scrapy'
    task_result = os.system("cd %s && scrapy crawl pm25" % pm_spider_dir)
    print task_result