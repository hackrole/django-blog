#!/usr/bin/python2.7
#charset=utf-8

from optparse import make_option
from django.conf import settings
from django.core.management.base  import BaseCommand,CommandError
from django.template import Template,Context,TemplateDoesNotExist,TemplateEncodingError,TemplateSyntaxError, loader
import json 
import codecs

class Command(BaseCommand):
    args = ''
    help = "try the template in console"
    option_list = BaseCommand.option_list + (
        make_option('--temp', action='store', dest='tfile', help='enter a temp file to try'
                    ),
        make_option('--context', action='store', dest='context', default='', help='enter a json style context for the template'
                    ),
        make_option('--write-file', action='store', dest='pfile', default='', help='enter a file path'
    ),
        )

    def handle(self, *args, **options):
        # print args
        # print options
        # return
        try:
            t = loader.get_template(options['tfile'])
        except TemplateDoesNotExist:
            print "template %s not exist" 
            return -1
        data = json.loads(options['context'])
        if not isinstance(data, dict):
            print "context option should be a dict like json"
        
        c = Context(data)
        output = t.render(c)
        if not options['pfile']:
            print output
        else:
            p = unicode(output)
            fp = codecs.open(options['pfile'], 'wb', 'utf-8')
            fp.write(p)
            fp.close()
        # raise CommandError('temp %s not exists' % self.temp)
        # except TemplateDoesNotExist,TemplateEncodingError,TemplateSyntaxError as e:
        #     print e.messages
        #     raise CommandError('template has error')

         
        
