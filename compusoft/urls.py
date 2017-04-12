#####################################################
#											   		#
#		CompuSoft - The Compushow 2017 Software	    #
#											   		#
#####################################################
#													#
#	- Main URL configuration file. Maps URLs to		#
#	  the nomination and voting modules.			#
#													#
#####################################################

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('nomination.urls')),
	url(r'^vote/', include('voting.urls')),
	url(r'^nominate/', include('nomination.urls')),
	url(r'^accounts/', include('nomination.urls')),
	url(r'^admin/', admin.site.urls),
]
