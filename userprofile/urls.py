__author__ = 'jorgezavala'
author__ = 'jorgezavala'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile', views.update_profile, name='profile'),
    url(r'^social_login$', views.social_login, name='social_login'),

]