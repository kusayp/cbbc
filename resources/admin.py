from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.


class SermonAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Sermon

class DevotionAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Devotion

class TeachingAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Teaching

admin.site.register(Sermon, SermonAdmin)
admin.site.register(Devotion, DevotionAdmin)
admin.site.register(Teaching, TeachingAdmin)