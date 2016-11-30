from django.shortcuts import render
from django.template.context import RequestContext

def home(request):
    print request

    context = ( {'request': request, 'user': request.user})


    return render(request, 'facebook.html', context, content_type='text/html')