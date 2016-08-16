from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.


class WelcomeAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "content"]
	class Meta:
		model = Welcome

class PastorAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "name"]
	class Meta:
		model = Pastor

admin.site.register(Welcome, WelcomeAdmin)
admin.site.register(Pastor, PastorAdmin)
