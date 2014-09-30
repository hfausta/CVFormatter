from django.db import models

# Create your models here.
class Account(models.Model):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 30)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()