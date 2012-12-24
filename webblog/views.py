# Create your views here.

from webblog.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    cate = Category.objects.all()
    tags = Tag.objects.all()
    
    return render_to_response('blog/index.html',{'cate':cate, 'tag':tags})
    # return HttpResponse('hello world, everybody')
    
def list(request, bid, btype):
    if btype == 1:
        data = Blog.objects.filter('category_id_id = %s' % bid)
    else:
        data = Blog_Tag.objects.filter(tag_id=bid)
    # data = [{'id':1, 'name':'emacs'}, {'id':2, 'name':'vim'}]

    return render_to_response('blog/list.html', {'data': data, 'bid': bid, 'btype': btype})

    
def detail(request, id):
    blog = Blog.objects.get(blog_id=id)
    print blog
    for i blog.
    return render_to_response('blog/detail.html', {'blog':blog,})
