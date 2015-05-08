from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def index(request):
        return render_to_response('blogindex.html')

@login_required
def admin(request):
	return render_to_response('admin.html')

#Logs the user out
def logout(request):
	auth_logout(request)
	args = {}
	args.update(csrf(request))
	return index(request)

def login(request):
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
	
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/blog/admin/')
		else:
			args = {}
			args.update(csrf(request))
			args['error'] = '**INVALID LOGIN CREDENTIALS**'
			return render_to_response('login.html',args)
	else:
		args = {}
		args.update(csrf(request))
		return render_to_response('login.html', args)

@login_required
def addproject(request):
	return render_to_response('addproject.html')
