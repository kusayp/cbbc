from django.contrib import admin
from django import forms
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ["__str__", "name", "is_prayer_request", "content" ]
	class Meta:
		model = Contact

class AddressAdmin(admin.ModelAdmin):
	list_display = ["__str__", "name"]
	class Meta:
		model = Address

admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)

