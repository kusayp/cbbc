from django.conf.urls import url

from . import views
# from resources import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^(?P<devotion_id>[0-9]+)/$', views.devotion_detail, name='devotion_detail'),
]