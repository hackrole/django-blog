#coding=utf-8

from django.contrib import admin
from webblog.models import *
from django.http import HttpResponse
from django.core import serializers
from django.contrib import admin
from django.http import HttpResponseRedirect

# def export_selected_objects(modeladmin, request, queryset):
#     selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#     ct = ContentType.objects.get_for_model(queryset.model)
#     return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected))

# admin.site.add_action(export_selected_objects, "export")

def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(mimetype="text/javascript")
    serializers.serialize("json", queryset, stream=response)
    return response

admin.site.add_action(export_as_json)

class BlogAdmin(admin.ModelAdmin):
    # pass
    actions = ['close_blog', 'pub_blog', 'show_blog']
    
    def close_blog(self, request, queryset):
        rows = queryset.update(is_close = True)
        message_bit = "%s blog were close" % rows
        self.message_user(request, "%s now" % message_bit)
    close_blog.short_description = "close the blog so it won't be show"
    def pub_blog(self, request, queryset):
        queryset.update(is_pub = True)
        response = HttpResponse(mimetype="text/javascript")
        serializers.serialize("json", queryset, stream=response)
        return response
    pub_blog.short_description = "publish this blog"
    def show_blog(self, request, queryset):
        for blog in queryset:
            blog.is_visiable = True
            blog.save()
    show_blog.short_description = "make this blog to be show"

class TagAdmin(admin.ModelAdmin):
    pass
    # action = ['']
        
def up_rate(modelAdmin, request, queryset):
    # queryset.update(category_rate=1)
    for cate in queryset:
        cate.category_rate = cate.category_rate + 1
        cate.save()
up_rate.short_description = "update the category rate by 1"

class CategoryAdmin(admin.ModelAdmin):
    # pass
    ordering = ['-category_pv']
    actions = [up_rate]
    

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)

