from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^event/', views.event, name='event'),
	url(r'^(?P<event_id>[0-9]+)/$', views.event_detail, name='event_detail')
]