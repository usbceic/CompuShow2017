#####################################################
#											   		#
#		CompuSoft - The Compushow 2017 Software	    #
#											   		#
#####################################################
#													#
#	- Main URL configuration file. Maps URLs to		#
#	  the voting app.								#
#													#
#####################################################

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('voting.urls')),
]
