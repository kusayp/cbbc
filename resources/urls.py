from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^sermon/', views.sermon, name='sermon'),
	url(r'^(?P<sermon_id>[0-9]+)/$', views.sermon_detail, name='sermon_detail'),
	url(r'^devotion/', views.devotion, name='devotion'),
	# url(r'^(?P<devotion_id>[0-9]+)/$', views.devotion_detail, name='devotion_detail'),
	url(r'^teaching/', views.teaching, name='teaching'),
	
]

#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),