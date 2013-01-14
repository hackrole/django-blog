#coding=utf8
# Create your views here.

from webblog.models import *
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from webblog.form import *
from django.core.mail import send_mail

def index(request):
    cate = Category.objects.all()
    tags = Tag.objects.all()
    
    return render_to_response('webblog/index.html',{'cate':cate, 'tag':tags})
    # return HttpResponse('hello world, everybody')
    
def cate(request, cate):
    if btype == 1:
        data = Blog.objects.filter('category_id_id = %s' % bid)
    else:
        data = Blog_Tag.objects.filter(tag_id=bid)
    # data = [{'id':1, 'name':'emacs'}, {'id':2, 'name':'vim'}]

    return render_to_response('blog/list.html', {'data': data, 'bid': bid, 'btype': btype})

def tag(request, tag):
    pass

def date(request, year, month):
    pass
    
def detail(request, id):
    blog = Blog.objects.get(blog_id=id)
    print blog
    # for i blog.
    return render_to_response('blog/detail.html', {'blog':blog,})

def about(request):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/blog/')
    
    form = AboutForm()
    about = About.objects.all()
    return render_to_response('blog/about.html', {'form':form, 'about':about}, context_instance=RequestContext(request))
     
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            admin_email = params.contact_email_admin.admin
            send_email('联系我们', form.cleaned_data.content, EMAIL_HOST_USER, ['daipeng123456@gmail.com'], fail_silently=False)
            if True == form.cleaned_data.if_accept_email:
                send_email('联系我们', form.cleaned_data.content, EMAIL_HOST_USER, [form.cleaned_data.email,], fail_silently=False)
            return render_to_response('tips.html')
    
    form = ContactForm()
    return render_to_response('blog/contact.html', {'form': form}, context_instance=RequestContext(request))

def post_comment(request):
    pass
