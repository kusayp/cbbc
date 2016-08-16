from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event
# Register your models here.

class EventAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "name", "theme", "date", "time", "date_posted"]
	class Meta:
		model = Event

admin.site.register(Event, EventAdmin)