#coding=utf8
# Create your views here.

from webblog.models import *
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from webblog.form import *
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import Http404
from django.template.response import TemplateResponse


def index(request, page=1):
    blogs = Blog.objects.order_by("-pub_time")
    p = Paginator(blogs, 3)
    try:
        blogs = p.page(page)
    except PageNotAnInteger:
        blogs = p.page(1)
    except EmptyPage:
        blogs = p.page(p.num_pages)

    # for blog in blogs:
    #     blog.comment_count = len(Comment.objects.filter(blog_id=blog.blog_id))

    return TemplateResponse(request, 'webblog/index.html', {'blogs':blogs})
    return render_to_response('webblog/index.html',context, context_instance=RequestContext(request))
    
def cate(request, cate, page=1):
    if cate is None:
        raise Http404

    blogs = Blog.objects.filter(category=Category.objects.get(category_id=cate))
    p = Paginator(blogs, 3)
    try:
        blogs = p.page(page)
    except PageNotAnInteger:
        blogs = p.page(1)
    except EmptyPage:
        blogs = p.page(p.num_pages)
    return TemplateResponse(request, 'webblog/index.html', {'blogs':blogs})
    return render_to_response('webblog/index.html', context, context_instance=RequestContext(request))

def tag(request, tid, page=1):
    if tag is None:
        raise Http404

    tag = Tag.objects.get(id=tid)
    blogs = tag.blog.filter(is_closed=False)
    p = Paginator(blogs, 3)
    try:
        blogs = p.page(page)
    except PageNotAnInteger:
        blogs = p.page(1)
    except EmptyPage:
        blogs = p.page(p.num_pages)
    return TemplateResponse(request, 'webblog/index.html', {'blogs':blogs})

def date(request, year, month):
    pass
    
def detail(request, id):
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog)
    commentForm = CommentForm()
    
    return render_to_response('webblog/detail.html', {'blog':blog,'comments':comments, 'form':commentForm})

def about(request, page=1):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/blog/')
    
    form = AboutForm()
    abouts = About.objects.all()
    p = Paginator(abouts, 6)
    try:
        abouts = p.page(page)
    except PageNotAnInteger:
        abouts = p.page(1)
    except EmptyPage:
        abouts = p.page(p.num_pages)
    return render_to_response('webblog/about.html', {'form':form, 'abouts':abouts}, context_instance=RequestContext(request))
     
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
    return render_to_response('webblog/contact.html', {'form': form}, context_instance=RequestContext(request))

def post_comment(request, id):
    if request.is_ajax() and request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            form.save()
