from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from forms import MessageForm

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('welcome!~' + request.GET['user_name'])

    else:
        return render_to_response('welcome.html', locals())

def index(request):
    return render(request, 'index.html', {'form': MessageForm()})