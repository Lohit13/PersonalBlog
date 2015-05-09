from django import forms 
from models import Project, Post


class ProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ('title','body','thumbnail','link',)

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title','body','image','tags',)
