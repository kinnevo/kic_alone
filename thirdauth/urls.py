__author__ = 'jorgezavala'

from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^signfb$', views.home, name='signfb'),
]


