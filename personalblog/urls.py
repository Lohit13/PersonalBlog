from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personalblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'personalblog.views.index', name='home'),  #Index Page
    url(r'^projects/$', 'personalblog.views.projects', name='projects'),  #Project List Page
    
    (r'^blog/', include('blog.urls')),	
)
