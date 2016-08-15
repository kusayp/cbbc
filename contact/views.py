from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import *
from .models import Address

def contact(request):
	address = Address.objects.order_by('-id')[:1]
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid:
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect('/home/')

	else:
		form = ContactForm()
	context = {
		'form':form,
		'address': address,
		'title': 'Contact',
	}
	return render(request, "contact.html", context)