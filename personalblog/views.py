from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def index(request):
	return render_to_response('index.html')

def projects(request):
	return render_to_response('projects.html')
