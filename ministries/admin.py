from django.contrib import admin
from .models import *
# Register your models here.


class MenAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Men

class WomenAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Women

class YouthAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Youth

class ChildrenAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Children

admin.site.register(Women, WomenAdmin)
admin.site.register(Men, MenAdmin)
admin.site.register(Youth, YouthAdmin)
admin.site.register(Children, ChildrenAdmin)