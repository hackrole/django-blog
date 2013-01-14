#!/usr/bin/python2.7
#coding=utf-8

from django.http import HttpResponse

class WebblogMiddleware(object):
    """
    add some common variable to the response
    """
    
    def process_template_response(self, request, response):
        print response.context_data
        return HttpResponse("hello world")
    
    def process_reponse(self, request, reponse):
        return HttpResponse('Hi world')

