from django.db import models

# Create your models here.

class Men(models.Model):
	"""
	model for Men

	"""
	name = models.CharField(max_length=100)
	content = models.TextField()
	time = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	notes = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Women(models.Model):
	"""
	model for Women

	"""
	name = models.CharField(max_length=100)
	content = models.TextField()
	time = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	notes = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Youth(models.Model):
	"""
	model for Youth

	"""
	name = models.CharField(max_length=100)
	content = models.TextField()
	time = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	notes = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Children(models.Model):
	"""
	model for Children

	"""
	name = models.CharField(max_length=100)
	content = models.TextField()
	time = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	notes = models.CharField(max_length=500)

	def __str__(self):
		return self.name