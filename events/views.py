from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def event(request):
	events = Event.objects.order_by('-id')[:1]
	context = {
		'events' : events,
		'title': 'Events',
	}
	return render(request, 'event.html', context)

def event_detail(request, event_id):
	events = get_object_or_404(Event, pk=event_id)
	context = {
		'events' : events,
		'title': 'Events',
	}
	return render(request, 'event_details.html', context)