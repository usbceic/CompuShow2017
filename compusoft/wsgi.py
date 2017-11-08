#####################################################
#											   		#
#		CompuSoft - The Compushow 2017 Software	    #
#											   		#
#####################################################
#													#
#	- entry-point for WSGI-compatible web 			#
#	  servers to serve CompuSoft.					#
#													#
#####################################################

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "compusoft.settings")

application = get_wsgi_application()
