#!/usr/bin/python2.7
#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from webblog.models import Tag

class WebblogMiddleware(object):
    """
    add some common variable to the response
    """
    
    def process_template_response(self, request, response):
        print response.context_data
        tags = Tag.objects.all()
        response.context_data['tags_new'] = tags
        for i in response.context_data:
            print i
        return response
        return render_to_response(response.template_name, response.context_data, context_instance=RequestContext(request))
    
    def process_response(self, request, reponse):
        # return HttpResponse('Hi world')
        return reponse
    def process_request(self, request):
        # return HttpResponse('hi hello')
        return None
