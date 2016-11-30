import json

from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def stats(request):

    users = 10
    ideas = 23
    comments = 100
    stats_info = {
        'users' : users,
        'ideas' : ideas,
        'comments' : comments,
    }

    data = []
    data.append( { 'type' : 'User25' , 'amount' : 6  })
    data.append( { 'type' : 'Zorrillo' , 'amount' : 5  })
    data.append( { 'type' : 'User 6' , 'amount' : 5  })
    data.append( { 'type' : 'User 26' , 'amount' : 5  })
    data.append( { 'type' : 'User 27' , 'amount' : 5  })
    data.append( { 'type' : 'Others' , 'amount' : 72  })


    json_string = json.dumps(data)


    return render(request, 'bar-chart.html', {'stats': stats_info , 'json_string' : json_string}, content_type='text/html')
#    return render(request, 'index.html', {'stats': stats_info }, content_type='text/html')

def simple_dashboard(request):

    users = 10
    ideas = 23
    comments = 100
    stats_info = {
        'users' : users,
        'ideas' : ideas,
        'comments' : comments,
    }
    data = []
    data.append( {'category': "Jorge", 'measure' : 0.30})
    data.append( {'category': "Peter", 'measure' : 0.25})
    data.append( {'category': "John", 'measure' : 0.15})
    data.append( {'category': "Rick", 'measure' : 0.05})
    data.append( {'category': "Lenny", 'measure' : 0.18})
    data.append( {'category': "Paul", 'measure' :0.04})
    data.append( {'category': "Steve", 'measure' : 0.03})

    json_string = json.dumps(data)

    return render(request, 'simple_dashboard.html', {'stats': stats_info , 'json_string' : json_string}, content_type='text/html')



def ajax(request):
    return render(request, 'ajax.html', {'stats': 'stats_info' , 'json_string' : 'json_string'}, content_type='text/html')

#from agent.daily.models import Ideas

def refresh(request):

    data = []
    data.append( {'category': "ZZZ", 'measure' : 0.30})
    data.append( {'category': "Peter", 'measure' : 0.25})
    data.append( {'category': "John", 'measure' : 0.15})
    data.append( {'category': "Rick", 'measure' : 0.05})
    data.append( {'category': "Lenny", 'measure' : 0.18})
    data.append( {'category': "Paul", 'measure' :0.04})
    data.append( {'category': "Steve", 'measure' : 0.03})

#    author = Ideas.objects.order_by('author').all().cont()
#    for idea in author:
#        print author.author

#    json_string = json.dumps(data)

    return JsonResponse(json.dumps(data), safe=False)