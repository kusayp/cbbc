from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def sermon(request):
	sermons = Sermon.objects.order_by('-id')[:1]
	context = {
		'sermons' : sermons,
		'title': 'Sermons',
	}
	return render(request, 'sermon/sermon.html', context)

def sermon_detail(request, sermon_id):
	sermons = get_object_or_404(Sermon, pk=sermon_id)
	context = {
		'sermons' : sermons,
		'title': 'Sermons',
	}
	return render(request, 'sermon/sermon_detail.html', context)

def devotion(request):
	devotions = Devotion.objects.order_by('-id')[:1]
	context = {
		'devotions' : devotions,
		'title': 'Devotions',
	}
	return render(request, 'devotion/devotion.html', context)

def devotion_detail(request, devotion_id):
	devotion = get_object_or_404(Devotion, pk=devotion_id)
	context = {
		'devotion' : devotion,
		'title': 'Devotions',
	}
	return render(request, 'devotion/devotion_detail.html', context)

def teaching(request):
	teachings = Teaching.objects.order_by('-id')[:1]
	context = {
		'teachings' : teachings,
		'title': 'Teachings',
	}
	return render(request, 'teaching/teaching.html', context)

def teaching_detail(request, teaching_id):
	teaching = get_object_or_404(Teaching, pk=teaching_id)
	context = {
		'teaching' : teaching,
		'title': 'Teachings',
	}
	return render(request, 'teaching/teaching_detail.html', context)
