from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import ProjectForm, PostForm
from models import Project, Post, Tag
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	args = {}
	posts = Post.objects.all()
	paginator = Paginator(posts, 10)
	page = request.GET.get('page')
        try:
	    posts = paginator.page(page)
        except PageNotAnInteger:
	    posts = paginator.page(1)
        except EmptyPage:
	    posts = paginator.page(paginator.num_pages)
	args['posts'] = posts
	args['tags'] = Tag.objects.all()
        return render_to_response('blogindex.html', args)

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

@login_required
def addpost(request):
	if request.POST:
		#files = upload_receive(request)
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			f2 = form.save(commit=False)
			f2.pub_date = datetime.now()
			f2.save()
			tags = f2.tags
			tags = tags.split(',')
			tagobjs = Tag.objects.all()
			taglist=[]
			for i in tagobjs:					#Adding new tags
				taglist.append(i.name)
			for i in tags:
				if i not in taglist:
					obj = Tag(name=i)
					obj.save()
					print 'saved'
					print obj
					print obj.name
					taglist.append(i)
			return HttpResponseRedirect('/blog/viewposts/')
		else:
			args = {}
			args.update(csrf(request))
			args['form']=form
			args['error']='Some error in form'
			return render_to_response('addpost.html',args)
				
	else:
		args = {}
		args.update(csrf(request))
		args['form'] = PostForm()
		return render_to_response('addpost.html',args)

@login_required
def viewposts(request):
	args = {}
	args['posts'] = Post.objects.all()
	return render_to_response('viewposts.html',args)

@login_required
def deletepost(request, post_id=1):
	try:
		post = Post.objects.get(id=post_id)
		post.delete()
		return HttpResponseRedirect('/blog/viewposts/')
	except:
		return HttpResponseRedirect('/blog/viewposts/')

def tagview(request, tag='1'):
	allposts = Post.objects.all()
	postlist = []
	for i in allposts:
		taglist=i.tags
		taglist=taglist.split(',')
		if tag in taglist:
			postlist.append(i)

	args={}
	args['tags'] = Tag.objects.all()

	posts = postlist
	paginator = Paginator(posts, 10)
	page = request.GET.get('page')
        try:
	    posts = paginator.page(page)
        except PageNotAnInteger:
	    posts = paginator.page(1)
        except EmptyPage:
	    posts = paginator.page(paginator.num_pages)
	args['posts'] = posts
	return render_to_response('blogindex.html',args)

def postview(request, post_id=1):
	post = Post.objects.get(id=post_id)
	args={}
	args['post']=post
	args['tags']=Tag.objects.all()
	return render_to_response('postview.html',args)
		
	

	
