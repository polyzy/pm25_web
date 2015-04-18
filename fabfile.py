__author__ = 'andy'
from fabric.api import local
def pre_deploy(branch_name='master'):
    local('python manage.py test pm25_web')
    local('git add --all')
    local('git commit')

def deploy():
    local('python manage.py migrate')
    local('python manage.py runserver')