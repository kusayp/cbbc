from django.db import models

# Create your models here.

class Sermon(models.Model):

    """
     Model for Sermon
    """
    date_posted = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(default=None)
    title= models.CharField(max_length=500)
    verse = models.CharField(max_length=1000, default='Hello')
    verse_name = models.CharField(max_length=100, default='Hello')
    content =  models.CharField(max_length=5000)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Devotion(models.Model):

    """
     Model for Devotion
    """
    date_posted = models.DateTimeField(auto_now_add=True)
    verse = models.CharField(max_length=1000)
    principle = models.CharField(max_length=1000)
    verse_name = models.CharField(max_length=100)
    title= models.CharField(max_length=500)
    content =  models.CharField(max_length=5000)
    
    def __str__(self):
        return self.title

class Teaching(models.Model):

    """
     Model for Teaching
    """
    title= models.CharField(max_length=500)
    content =  models.CharField(max_length=5000)
    
    def __str__(self):
        return self.title