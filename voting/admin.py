#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  	 			  - Admin site file.   				#
#  													#
#####################################################

from django.contrib import admin
from .models import *

class NomineeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nominations', 'votes', 'category', 'entity', 'entityOpt', 'extra']
    list_filter = ['category']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['ci', 'name', 'surname', 'email']
admin.site.register(Entity)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Nominate)
admin.site.register(Nominee, NomineeAdmin)
admin.site.register(Winner)