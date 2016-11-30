__author__ = 'jorgezavala'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stats', views.stats, name='stats'),
    url(r'^simple_dashboard', views.simple_dashboard, name='simple_dashboard'),

    url(r'^ajax', views.ajax, name='ajax'),
    url(r'^refresh', views.refresh, name='refresh'),

]