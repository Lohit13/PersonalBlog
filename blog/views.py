from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import ProjectForm
from models import Project

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
	if request.user.is_authenticated():
		return HttpResponseRedirect('/blog/admin/')
	else:
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
	if request.POST:
		#files = upload_receive(request)
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			f2 = form.save(commit=False)
			f2.save()
			return HttpResponseRedirect('/blog/viewprojects/')
		else:
			args = {}
			args.update(csrf(request))
			args['form']=form
			args['error']='Some error in form'
			return render_to_response('addproject.html',args)
				
	else:
		args = {}
		args.update(csrf(request))
		args['form'] = ProjectForm()
		return render_to_response('addproject.html',args)

@login_required
def viewprojects(request):
	args = {}
	args['projects'] = Project.objects.all()
	return render_to_response('viewprojects.html',args)

@login_required
def deleteproject(request, prj_id=1):
	try:
		prj = Project.objects.get(id=prj_id)
		prj.delete()
		return HttpResponseRedirect('/blog/viewprojects/')
	except:
		return HttpResponseRedirect('/blog/viewprojects/')
	
