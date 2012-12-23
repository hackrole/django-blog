# Create your views here.

from webblog.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
def index(request):
    cate = Category.objects.all()
    tags = Tags.objects.all()
    
    return render_to_response('blog/index.html',{'cate':cate})
    # return HttpResponse('hello world, everybody')
    
