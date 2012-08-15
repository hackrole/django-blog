from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib import auth
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    return render_to_response('time.html',{'time' : now ,})

#def add_blog(request):
    #name = request.GET.get('name','')
    #now = datetime.datetime.now()
    #if !name:
        #return render_to_response('time.html',{'time':now})
    #return render_to_response('form.html')

def login(request):
    if request.user.is_authenticated():
        return render_to_response('login/logsuc.html')
    return render_to_response('login/log.html')

def logon(request):
    if request.method == 'post':
        name = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("/login/")
    return render_to_response('error.html')

def (request):

    return render_to_response('',{})

# vim:st=4:sts=4:sw=4:et
