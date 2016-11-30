# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db import models
from django.http import JsonResponse
import json
from django.db.models import Count, Min, Sum, Avg



from models import *

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
        category = request.POST.get('category')
        comment = request.POST.get('comment')

#        author = request.POST.get( 'author')
#        author = "Jorge"
        date_now = date.today()
#        date_now = time.strftime("%c")


        i = Ideas(date=date_now, author=author, description=idea, votes=0)
        i.save()

#        j = IdeaComment(comment=comment )
#        j.save()
# category=category

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

from .forms import IdeaForm, CommentForm, CategoryForm

def new_idea(request):
    if request.user.is_authenticated:
        author = request.user

        if request.method == 'POST':
            form1 = IdeaForm(request.POST)
            form3 = CategoryForm(request.POST)

            if form1.is_valid()  and form3.is_valid():
                today = date.today()
                author = request.user
                idea = request.POST.get('description')

                i_idea = Ideas( author=author, description=idea,votes=0, date=today)
                i_idea.save()

                category = request.POST.get('category')

                i_category = IdeaCategory(category=category, idea=i_idea)
                i_category.save()

                return render(request, 'new_idea.html', {'form1': form1})
        else:
            form1 = IdeaForm()
#            form2 = CommentForm()
            form3 = CategoryForm()
            return render(request, 'new_idea.html', {'form1': form1, 'form3' : form3})

    else:
        return redirect('/login/?next=/daily/new_idea')

def nurture_idea(request, pk, template_name='ideas/nurture_idea.html'):
    if request.user.is_authenticated:

#    print "PK in nurture_idea: ", pk

        idea_ref = get_object_or_404(Ideas, pk=pk)

        comments = IdeaComment.objects.filter(idea=pk).all()
        count = IdeaComment.objects.filter(idea=pk).all().count()
        author = request.user.username

        categories = IdeaCategory.objects.filter(idea=pk).all()
        category = ""
        first_category = True
        for cat in categories:
            if first_category == True:
                category = cat.category
                first_category = False
            else:
                category =  category + ", " + cat.category
    #    print "xxx: ",category

    #    child_of_bob = Child.objects.get(parent__name="Bob")
    #    for c in comments:
    #        print c.comment

        if request.method == 'POST':
            comment = request.POST.get('comment')
            if (comment <> ""):
                i_comment = IdeaComment(comment=comment, idea=idea_ref, author=author )
                i_comment.save()
            else:
                print "PPPPPPOST: No hay comentario"

            return render(request, template_name, {'idea': idea_ref, 'count': count, 'comments' : comments,  'category' : category })
        else:
            return render(request, template_name, {'idea': idea_ref, 'count': count, 'comments' : comments , 'category' : category})

    else:
        return redirect('/login/?next=/daily/report')



def ajax1(request):
    return render(request, 'ajax1.html', {'stats': 'stats_info' , 'json_string' : 'json_string'}, content_type='text/html')

from models import Ideas
from django.db.models import Count




"""
    data.append( {'category': "XXX", 'measure' : 0.30})
    data.append( {'category': "Peter", 'measure' : 0.25})
    data.append( {'category': "John", 'measure' : 0.15})
    data.append( {'category': "Rick", 'measure' : 0.05})
    data.append( {'category': "Lenny", 'measure' : 0.18})
    data.append( {'category': "Paul", 'measure' :0.04})
    data.append( {'category': "Steve", 'measure' : 0.03})
"""
def refresh1(request):

    data = []

    authors = Ideas.objects.annotate(num_ideas=Count('author', distinct=True)).order_by('author')
#    print "Counter: ", authors[0].author__count, "\n"
#    for idea in authors:
#        print idea.num_ideas, idea.author

#        print authors[0].num_ideas, authors[0].author

    authors = Ideas.objects.all().aggregate(Count('author'))
    total_ideas = authors['author__count']
#    print "Total number of ideas: ", total_ideas

 #   a = Ideas.objects.all()

    b = Ideas.objects.values('author').annotate(count=Count('author'))[:5]

#    print authors, "\na: ", a, "\nb: ", b

    partial = 0
    for x in b:
        partial += x['count']
#        print "Author: ", x['author'], ":", x['count']
#        print "Author: ", x.author, ":", x.count
        data.append( {'category': x['author'] , 'measure' : x['count']})

    difference = total_ideas - partial
#    print "Partial: ",  partial, "difference", difference
    data.append( {'category': 'others' , 'measure' : difference })

#    json_string = json.dumps(data)

#    json_data = { 'data' : data, 'ideas' : total_ideas}

    return JsonResponse(json.dumps(data), safe=False)