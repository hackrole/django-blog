#!/usr/bin/python2.7
#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from webblog.models import *
from django.db.models import Count

class WebblogMiddleware(object):
    """
    add some common variable to the response
    """
    
    def process_template_response(self, request, response):
        # print response.context_data
        tags = {}
        tags['count'] = Tag.objects.count()
        tags['tags'] = Tag.objects.all()[0:6]
        cate = {}
        cate['count'] = Category.objects.count()
        cate['cates'] = Category.objects.all()[0:6]
        hotcomment = Comment.objects.filter(is_close=False)[0:5]
        mostcomment = Comment.objects.aggregate(blog_count=Count(blog_id), distinct=True)[0:6]
        
        response.context_data['tags'] = tags
        response.context_data['cate'] = cate
        response.context_data['hotcom'] = hotcomment
        response.context_data['mostcom'] = mostcomment

        return response
        return render_to_response(response.template_name, response.context_data, context_instance=RequestContext(request))
    
    def process_response(self, request, reponse):
        # return HttpResponse('Hi world')
        return reponse
    def process_request(self, request):
        # return HttpResponse('hi hello')
        return None
