from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^thanks', views.appreciation, name='appreciation'),
	url(r'^contact/', views.contact, name='contact'),
]