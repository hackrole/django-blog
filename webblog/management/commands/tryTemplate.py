#!/usr/bin/python2.7
#charset=utf-8

from optparse import make_option
from django.conf import settings
from django.core.management.base  import BaseCommand,CommandError
from django.template import Template,Context,TemplateDoesNotExist,TemplateEncodingError,TemplateSyntaxError
import json 

class Command(BaseCommand):
    args = ''
    help = "try the template in console"
    option_list = AppCommand.option_list + (
        make_option('--temp', action='store', dest='temp file', help='end a temp file to try'
                    ),
        make_option('--context', action='store', dest='context data', default='', help='enter a json style context for the template'
                    ),
        )

    def handle(self, *args, **options):
        try:
            s = open(self.temp).read()
            t = Template(s)
            data = json.read(self.context)
            c = Context(data)
            output = t.render(c)
            print output
        except IOError as e:
            raise CommandError('temp %s not exists' % self.temp)
        except TemplateDoesNotExist,TemplateEncodingError,TemplateSyntaxError as e:
            print e.messages
            raise CommandError('template has error')
        finally:
            s.close()

         
        
