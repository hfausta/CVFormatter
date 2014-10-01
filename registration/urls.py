from django.conf.urls import patterns, url

# import views from registration module
from registration import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^register$', views.register, name = 'register'),
)