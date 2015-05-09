from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
	return "%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	thumbnail = models.ImageField(upload_to=get_upload_file_name, blank=True, null=True)
	link = models.TextField()

	def __unicode__(self):
		return self.title



