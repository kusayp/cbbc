from django.shortcuts import render
from .models import *

def hymn(request):
	details = Hymn.objects.order_by('name')
	context = {
		'titles' : details,
		'title': 'Hymn',
	}
	return render(request, 'hymn_ls.html', context)

def stanza_detail(request, hymn_id):
	# hymn = Hymn.objects.get()
    details = Hymn.objects.get(id = hymn_id)
    has_refrain = details.has_refrain
    refrain = details.refrain
	# print(refrain)
    stanza = details.stanzas.all()
    context = {
        'name' : details,
		'hymn' : refrain,
		'titles' : stanza,
		'title': 'Hymn Details',
        'has_refrain': has_refrain,
	}
    return render(request, 'hymn.html', context)
