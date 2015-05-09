from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from blog.models import Project

def index(request):
	return render_to_response('index.html')

def projects(request):
	args={}
	args['projects'] = Project.objects.all()
	return render_to_response('projects.html',args)
