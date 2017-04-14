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

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import url, include

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('voting.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)