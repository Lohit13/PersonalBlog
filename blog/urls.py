from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^$', 'blog.views.index', name='bloghome'),  #Index Page 
    url(r'^adminlogin/', 'blog.views.login', name='admin'),  #Site Admin Page 
    url(r'^logout/', 'blog.views.logout'), #Logs out the admin
    url(r'^admin/', 'blog.views.admin'), #Admin view
    url(r'^addproject/', 'blog.views.addproject', name='addproject'),  #Add Project
    url(r'^viewprojects/', 'blog.views.viewprojects', name='viewprojects'),  #View All Project
    url(r'^deleteproject/(?P<prj_id>\d+)/$', 'blog.views.deleteproject', name='deleteproject'), #Delete project

)
