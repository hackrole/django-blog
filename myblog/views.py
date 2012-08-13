from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    return render_to_response('time.html',{'time' : now ,})

def add_blog(request):
    name = request.GET.get('name','')
    now = datetime.datetime.now()
    if !name:
        return render_to_response('time.html',{'time':now})
    return render_to_response('form.html')

def login(request):

