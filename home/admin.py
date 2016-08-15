from django.contrib import admin
from .models import *
# Register your models here.


class WelcomeAdmin(admin.ModelAdmin):
	list_display = ["__str__", "content"]
	class Meta:
		model = Welcome

class PastorAdmin(admin.ModelAdmin):
	list_display = ["__str__", "name"]
	class Meta:
		model = Pastor

admin.site.register(Welcome, WelcomeAdmin)
admin.site.register(Pastor, PastorAdmin)
