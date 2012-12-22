# Create your views here.

from webblog.models import *
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world, everybody')
    
