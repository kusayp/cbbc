from django.shortcuts import get_object_or_404, render
from .models import *
from events.models import Event
from resources.models import Devotion

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

# def search_helper(count, query):
#         import itertools
#         model_list = Hymn.objects.filter(name__icontains=query, status=1)
#         for L in range(1, count+1):
#                 for subset in itertools.permutations(words, L):
#                         count1=1
#                         query1=subset[0]
#                         while count1!=len(subset):
#                                 query1=query1+" "+subset[count1]
#                                 count1+=1
#                         model_list = entry_list | Hymn.objects.filter(name__icontains=query1, status=1)
#         return (model_list.distinct())

def devotion_detail(request, devotion_id):
        devotion = get_object_or_404(Devotion, pk=devotion_id)
        context = {
                'devotion' : devotion,
                'title': 'Devotions',
        }
        return render(request, 'devotion/devotion_detail.html', context)