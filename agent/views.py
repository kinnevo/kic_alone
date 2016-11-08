__author__ = 'jorgezavala'

from django.http import HttpResponse
from django.shortcuts import render

def index1(request):
    return HttpResponse("The top level.")


def home(request):
    return render(request, 'home.html', {'ideas': 'ideas' }, content_type='text/html')


def blog(request):
    return render(request, 'blog.html', {'ideas': 'ideas'}, content_type='text/html')

def blog1(request):
    return render(request, 'blog1.html', {'ideas': 'ideas'}, content_type='text/html')
