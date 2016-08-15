from django.db import models
# Create your models here.

class Event(models.Model):
	"""
	model for welcome

	"""
	theme = models.CharField(max_length=100)
	theme_verse = models.CharField(max_length=100)
	verse = models.CharField(max_length=500)
	name = models.CharField(max_length=100)
	details = models.CharField(max_length=1000)
	location = models.CharField(max_length=300)
	time = models.TimeField(auto_now_add=False)
	date = models.DateField(auto_now_add=False)
	date_posted = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name


