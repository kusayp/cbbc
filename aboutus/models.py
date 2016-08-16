from django.db import models

# Create your models here.

class WWB(models.Model):
	"""
	model for what we believe

	"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	verses = models.CharField(max_length=500)
	notes = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Message(models.Model):
	"""
	model for what we believe

	"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	verses = models.CharField(max_length=500)
	notes = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title