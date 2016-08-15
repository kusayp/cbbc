from django.shortcuts import render
from .models import *
from events.models import Event

# Create your views here.
def home(request):
	details = Welcome.objects.order_by('-id')[:1]
	pastors = Pastor.objects.order_by('-id')[:1]
	events = Event.objects.order_by('-id')[:1]
	context = {
		'events' : events,
		'titles' : details,
		'pastors' : pastors,
		'title': 'Home',
	}
	return render(request, 'home.html', context)
