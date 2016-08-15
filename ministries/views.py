from django.shortcuts import render

# Create your views here.
from .models import *

# Create your views here.
def men(request):
	mens = Men.objects.order_by('-id')[:1]
	# time = mens.time
	# place = mens.location
	context = {
		'mens' : mens,
		# 'time' : time,
		# 'place' : place,
		'title': 'Men Fellowship',
	}
	return render(request, 'men.html', context)


def women(request):
	womens = Women.objects.order_by('-id')[:1]
	# time = womens.time
	# place = womens.location
	context = {
		'womens' : womens,
		# 'time' : time,
		# 'place' : place,
		'title': 'Women Fellowship',
	}
	return render(request, 'women.html', context)


def youth(request):
	youths = Youth.objects.order_by('-id')[:1]
	# time = youth.time
	# place = youth.location
	context = {
		'youths' : youths,
		# 'time' : time,
		# 'place' : place,
		'title': 'Youth Fellowship',
	}
	return render(request, 'youth.html', context)


def children(request):
	childrens = Men.objects.order_by('-id')[:1]
	time = childrens.time
	place = childrens.location
	context = {
		'childrens' : childrens,
		# 'time' : time,
		# 'place' : place,
		'title': 'Children Fellowship',
	}
	return render(request, 'children.html', context)
