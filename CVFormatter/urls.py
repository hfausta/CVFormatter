from django.conf.urls import patterns, include, url
from django.contrib import admin

import registration
from registration import views

urlpatterns = patterns('',
		# Examples:
		# url(r'^registration/', include('registration.urls')),
		url(r'^$', registration.views.index, name = 'index'),
		url(r'^register/$', registration.views.register, name = 'register'),
		# url(r'^blog/', include('blog.urls')),

		url(r'^admin/', include(admin.site.urls)),
)
