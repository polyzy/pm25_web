__author__ = 'andy'
from django.db import models


# class CityManager(models.Manager):
# def safe_get(self, id):
# try:
#             city = City.objects.get(id=id)
#         except City.DoesNotExist:
#             city = None
#         return city
# class DataManager(models.Manager):
#     def safe_get(self, id):
#         try:
#             city = City.objects.get(id=id)
#         except City.DoesNotExist:
#             city = None
#         return city

class ModelManager(models.Manager):
    def safe_get(self, id):
        try:
            obj = self.get(id=id)
        except Exception:
            obj = None
        return obj
