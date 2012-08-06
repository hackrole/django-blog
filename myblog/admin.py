from myblog.models import BlogAside,BlogMolu,BlogArtcle,BlogTags
from django.contrib import admin


class BlogMoluInline(admin.StackedInline):
    model = BlogMolu
    extra = 3

class BlogAsideAdmin(admin.ModelAdmin):
    fields = ['name', 'sortNum', 'desc']
    inlines = [BlogMoluInline]

class BlogMoluAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields':['name','sortNum','status']}),
            ('Data information', {'fields':['desc','add_time'], 'classes':['collapse']}),
    ]
admin.site.register(BlogMolu, BlogMoluAdmin)
admin.site.register(BlogAside, BlogAsideAdmin)
