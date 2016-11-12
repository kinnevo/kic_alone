__author__ = 'jorgezavala'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^getideas$', views.getideas, name='getideas'),
    url(r'^filter', views.filter, name='filter'),
    url(r'^logged_actions', views.logged_actions, name='filter'),
    url(r'^report', views.report, name='report'),
    url(r'^search_by_author', views.search_by_author, name='search_by_author'),
    url(r'^idea_edit/(?P<pk>\d+)$', views.idea_update, name='idea_edit'),
    url(r'^idea_delete/(?P<pk>\d+)$', views.idea_delete, name='idea_delete'),
    url(r'^new_idea$', views.new_idea, name='new_idea'),

    url(r'^nurture_idea/(?P<pk>\d+)$', views.nurture_idea, name='nurture_idea'),

]
