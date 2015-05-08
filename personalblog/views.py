from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from models import Project

def index(request):
	return render_to_response('index.html')

def projects(request):
	return render_to_response('projects.html')
