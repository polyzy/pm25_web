__author__ = 'andy'
from fabric.api import local
def prepare_deployment(branch_name):
    local('python manage.py test pm25_web')
    local('git add --all && git commit')