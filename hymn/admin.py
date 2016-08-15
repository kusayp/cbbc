from django.contrib import admin

# Register your models here.

from .models import *
# Register your models here.

class HymnAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	search_fields = ('name','refrain')
	class Meta:
		model = Hymn

class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Category

class StanzaAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Stanza

admin.site.register(Hymn, HymnAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stanza, StanzaAdmin)