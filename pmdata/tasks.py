__author__ = 'andy'


from celery import task

@task
def fetch_pm_data():
    print 'fetch data by python scrapy'