from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^wwb/', views.wwb, name='wwb'),
	url(r'^message/', views.message, name='message'),
	url(r'^(?P<teaching_id>[0-9]+)/$', views.teaching_detail, name='teaching_detail'),
]