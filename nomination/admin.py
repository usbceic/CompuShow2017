#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  	 - Admin site file of the nomination module.    #
#  													#
#	   Superuser: 									#
#			username: compusoft 					#
#			password: ceic traditional password		#
#                                                   #
#####################################################

from django.contrib import admin
from .models import *

admin.site.register(Entity)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Nominate)
admin.site.register(Nominee)
admin.site.register(Winner)