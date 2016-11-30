"""agent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^accounts/login/$', auth_views.login, name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^daily/', include('daily.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^blog1$', views.blog1, name='blog1'),

    url(r'^servers/', include('servers.urls')),
    url(r'^books_fbv_user/', include('books_fbv_user.urls')),
    url(r'^userprofile/', include('userprofile.urls')),
    url(r'^facebook/', include('thirdauth.urls')),

    url(r'^stats/', include('stats.urls')),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),



    url(r'^index1', views.index1, name='index1'),
    url(r'^home/', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^', views.home, name='home'),
]

