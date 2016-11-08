from django.shortcuts import render,render_to_response
from django.template import RequestContext
# Create your views here.

def showrec(request):
    show = "hello World"
    return render_to_response('showrec.html',locals())

def subject(request):
    postcontent=""
    if request.POST:
        for i in request.POST:
            postcontent += i + "=>" + request.POST[i] + ","
    return render_to_response('subject.html', RequestContext(request, locals()))