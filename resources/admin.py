from django.contrib import admin
from .models import *
# Register your models here.


class SermonAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Sermon

class DevotionAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Devotion

class TeachingAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Teaching

admin.site.register(Sermon, SermonAdmin)
admin.site.register(Devotion, DevotionAdmin)
admin.site.register(Teaching, TeachingAdmin)