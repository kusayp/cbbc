from django.shortcuts import render
from .models import *

# Create your views here.
def wwb(request):
	wwbs = WWB.objects.order_by('-id')[:1]
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