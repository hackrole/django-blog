from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog import settings
from webblog.models import BlogSitemap
from django.contrib.sitemaps import views as sitemaps_views
from django.views.decorators.cache import cache_page

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

urlpatterns += patterns('',
                        url(
        r'^blog/sitemap\.xml/$', 
        cache_page(86400)(sitemaps_views.sitemap),#'django.contrib.sitemaps.views.sitemap', 
        {'sitemaps':{'blog':BlogSitemap}}
        ),
)

urlpatterns += patterns('webblog',
                        url(r'^blog/(?P<page>\d+)/$', 'views.index'),
                        url(r'^blog/$', 'views.index'),
                        url(r'^blog/cate/(\d+)/(?P<page>\d+)/$', 'views.cate'),
                        url(r'^blog/cate/(\d+)/$', 'views.cate'),
                        url(r'^blog/tag/(\d+)$', 'views.tag'),
                        url(r'^blog/id/(?P<id>\d+)$', 'views.detail'),
                        url(r"^blog/comment/$", 'views.post_comment'),
                        url(r'^blog/about/(\d+)$', 'views.about'),
                        url(r'^blog/about/$', 'views.about'),
                        url(r'^blog/contact/$', 'views.contact'),
                        url(r'^blog/source/$', 'views.source'),
                        
)
if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
