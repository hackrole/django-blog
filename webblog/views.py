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

cate_count = Category.objects.count()
cate = Category.objects.all()[0:10]
context = {
    'cate_count':cate_count,
    'cate':cate,
    }

def index(request, page=1):
    global context
    cate_count = Category.objects.count()
    cate = Category.objects.all()[0:10]
    tags_count = Tag.objects.count()
    tags = Tag.objects.all()
    hotComment_count = Comment.objects.count()
    hotComment = Comment.objects.filter(is_close=False,is_discard=False).order_by("comment_level")[0:10]
    
    hotBlog = Comment.objects.raw("select count(blog_id) ad comment_count from webblog_comment where blog_id is not null and is_close!=FALSE and is_discard!=FALSE group by blog_id order by comment_count limit 10")

    blogs = Blog.objects.filter(is_pub=True).order_by("-pub_time")
    p = Paginator(blogs, 3)
    try:
        blogs = p.page(page)
    except PageNotAnInteger:
        blogs = p.page(1)
    except EmptyPage:
        blogs = p.page(p.num_pages)

    for blog in blogs:
        blog.comment_count = len(Comment.objects.filter(blog_id=blog.blog_id))

    context['tags_count'] = tags_count
    context['tags'] = tags
    context['blogs'] = blogs
    return render_to_response('webblog/index.html',context, context_instance=RequestContext(request))
    
def cate(request, cate, page=1):
    global context
    if cate is None:
        raise Http404
    blogs = Blog.objects.filter(category_id__category_id=cate)
    p = Paginator(blogs, 3)
    try:
        blogs = p.page(page)
    except PageNotAnInteger:
        blogs = p.page(1)
    except EmptyPage:
        blogs = p.page(p.num_pages)
    context['blogs'] = blogs
      
    return render_to_response('webblog/index.html', context, context_instance=RequestContext(request))

def tag(request, tag):
    pass

def date(request, year, month):
    pass
    
def detail(request, id):
    blog = Blog.objects.get(blog_id=id)
    comments = Comment.objects.filter(blog_id=id).order_by('comment_level')
    commentForm = CommentForm()
    
    return render_to_response('webblog/detail.html', {'blog':blog,'comments':comments, 'form':commentForm})

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

def post_comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        blog = Blog.objects.get(blog_id=id)
        # if form.is_valid:
        #     form.
