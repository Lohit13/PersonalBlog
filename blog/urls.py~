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
    url(r'^addpost/', 'blog.views.addpost', name='addpost'),  #Add Post
    url(r'^viewposts/', 'blog.views.viewposts', name='viewposts'),  #View All Posts
    url(r'^deletepost/(?P<post_id>\d+)/$', 'blog.views.deletepost', name='deletepost'), #Delete post
    url(r'^view/(?P<tag>\w+)/$', 'blog.views.tagview', name='tagview'), #View posts with certain tag
    url(r'^post/(?P<post_id>\d+)/$', 'blog.views.postview', name='postview'), #Single post view

)
