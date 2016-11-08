# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db import models

from models import Ideas

from datetime import date
import time

def index(request):
    print request, "Index\n"

    return HttpResponse("Hello, world. You're at the daily index.")



def dashboard(request):
     # print request, "Dashboard\n"

     # return HttpResponse("hi, soy DASHBOARD.")

     ideas = Ideas.objects.order_by('description').all()


#     print "IDEAS: ", ideas, ideas.count(), "\n\n"
#     for i in range(ideas.count()):
#        print ideas[i].author, "\n"

     return render(request, 'dashboard.html', {
        'ideas': ideas,
         }, content_type='text/html')


def getideas(request):
    ideas = []
    idea = "Empty"

    if request.user.is_authenticated:
        author = request.user
#        print author, ": is logged\n"
    else:
        author = "anonymous"
#        print "no logged user, your ideas are going to be register as anonymous"

    if request.method == 'POST':
        idea = request.POST.get('idea')
#        author = request.POST.get( 'author')
        date_now = date.today()
#        date_now = time.strftime("%c")

#        author = "Jorge"

        i = Ideas(date=date_now, author=author, description=idea)
        i.save()

        ideas = Ideas.objects.order_by('description').all()


    return render(request, 'getideas.html', {'ideas': ideas}, content_type='text/html')

def filter(request):
    ideas = []
    if request.method == 'POST':
        keyword = request.POST.get('keyword')

        ideas = Ideas.objects.filter(description__icontains=keyword)

    return render(request, 'filter.html', {'ideas': ideas}, content_type='text/html')

def logged_actions(request):
    ideas = []

    return render(request, 'logged_actions.html', {'ideas': ideas}, content_type='text/html')

from django.db.models import Count

def report(request):
    ideas = []

#    count1 = Ideas.objects.filter(author='Jorge' ).count()
#    count2 = Ideas.objects.filter(author='jorge' ).count()
#    count3 = Ideas.objects.filter(author='anonymous' ).count()
#
#    print count1, count2, count3

    ideas = Ideas.objects.values('author').annotate(Count('author')).order_by('-author__count')

#    for i in ideas:
#        print i, "\n"


    return render(request, 'report.html', {'ideas': ideas}, content_type='text/html')

def search_by_author(request):
    ideas = []

    author = request.GET['author']
#    print author
    ideas = Ideas.objects.filter(author=author)

    return render(request, 'search_by_author.html', {'ideas': ideas, 'author':author}, content_type='text/html')


class IdeasForm(ModelForm):
    class Meta:
        model = Ideas
        fields = ['description', 'author']

def idea_update(request, pk, template_name='ideas/idea_form.html'):
    server = get_object_or_404(Ideas, pk=pk)
    form = IdeasForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('report')
    return render(request, template_name, {'form':form})


def idea_delete(request, pk, template_name='ideas/idea_confirm_delete.html'):
    ideas = get_object_or_404(Ideas, pk=pk)
    if request.method=='POST':
        ideas.delete()
        return redirect('report')
    return render(request, template_name, {'object':ideas})
