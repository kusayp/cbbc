from django.shortcuts import get_object_or_404, render
from .models import *
from resources.models import Teaching

# Create your views here.
def wwb(request):
	wwbs = WWB.objects.order_by('-id')
	context = {
		'wwbs' : wwbs,
		'title': 'What We Believe',
	}
	return render(request, 'wwb.html', context)


def message(request):
	messages = Message.objects.order_by('-id')[:1]
	context = {
		'messages' : messages,
		'title': 'Salvation Message',
	}
	return render(request, 'message.html', context)

def teaching_detail(request, teaching_id):
	teaching = get_object_or_404(Teaching, pk=teaching_id)
	context = {
		'teaching' : teaching,
		'title': 'Teachings',
	}
	return render(request, 'teaching/teaching_detail.html', context)