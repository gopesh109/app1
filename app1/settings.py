from django_core.settings import *

INSTALLED_APPS += [
    'app1',
    'shared_models',
]

ROOT_URLCONF = 'app1.urls'
