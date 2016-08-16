from django.db import models 


class Contact(models.Model): 
	"""
	model for Contact

	"""
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	is_prayer_request = models.BooleanField(default=False)
	content = models.CharField(max_length=2000)

	def __str__(self):
		return self.name

class Address(models.Model):
	"""
	model for Address

	"""
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	box = models.CharField(max_length=2000)
	location = models.CharField(max_length=1000)
	notesadd = models.TextField()
	notescont = models.TextField()

	def __str__(self):
		return self.name
