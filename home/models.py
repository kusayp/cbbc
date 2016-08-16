from django.db import models

# Create your models here.

class Welcome(models.Model):
	"""
	model for welcome

	"""
	date_posted = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	content = models.TextField()
	pastor = models.CharField(max_length=100)
	note = models.TextField()

	def __str__(self):
		return self.title

class Pastor(models.Model):
	"""
	model for pastors

	"""
	date_posted = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	background = models.TextField()
	phone = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	
	def __str__(self):
		return self.name