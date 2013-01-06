#!/usr/bin/python2.7
#charset=utf-8

from django.core.management.base import BaseCommand, CommandError
from webblog.models import Contact

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        
