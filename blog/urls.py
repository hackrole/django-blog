from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



urlpatterns += patterns('webblog',
                        url(r'^blog/$', 'views.index'),
                        url(r'^blog/cate/(\w+)$', 'views.cate'),
                        url(r'^blog/tag/(\w+)$', 'views.tag'),
                        # url(r'^blog/(\d{4})/(\d{2})$', 'views.data'),
                        url(r'^blog/blog/(?P<id>\d+)$', 'views.detail'),
                        url(r"^blog/comment/$", 'views.post_comment'),
                        url(r'^blog/about/$', 'views.about'),
                        url(r'^blog/contact/$', 'views.contact'),
)
if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
