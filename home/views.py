from django.shortcuts import get_object_or_404, render
from .models import *
from events.models import Event
from resources.models import Devotion

# Create your views here.
def home(request):
	details = Welcome.objects.order_by('-id')[:1]
	pastors = Pastor.objects.order_by('-id')[:3]
	events = Event.objects.order_by('-id')[:1]
	context = {
		'events' : events,
		'titles' : details,
		'pastors' : pastors,
		'title': 'Home',
	}
	return render(request, 'home.html', context)

def devotion_detail(request, devotion_id):
        devotion = get_object_or_404(Devotion, pk=devotion_id)
        context = {
                'devotion' : devotion,
                'title': 'Devotions',
        }
        return render(request, 'devotion/devotion_detail.html', context)