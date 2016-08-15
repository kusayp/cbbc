from django.contrib import admin
from .models import *
# Register your models here.

class WWBAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = WWB

class MessageAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Message

admin.site.register(WWB, WWBAdmin)
admin.site.register(Message, MessageAdmin)