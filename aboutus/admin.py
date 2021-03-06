from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.

class WWBAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = WWB

class MessageAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Message

admin.site.register(WWB, WWBAdmin)
admin.site.register(Message, MessageAdmin)