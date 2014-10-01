from django.db import models

# Create your models here.
class Account(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 30)
	created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)
	
	# for admin purposes, returning the object identity
	def __unicode__(self):
		return self.username
