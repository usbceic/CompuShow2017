#!/usr/bin/python3
#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#        - Check Status of Nominations.  	    #
#                                                   #
#####################################################

import os
import sys
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'compusoft.settings'
django.setup()

from voting.library import *

def main():

	results = get_nominees(1000)
	
	for category, nominees in results.items():

		# Specify categories to be displayed in the console
		if len(sys.argv) <= 1 or category.name in sys.argv[1:]:

			print("-------------------------------")
			print("Category: " + str(category.name))
			
			if not nominees:
				print("\tNone")
			
			ranking = 1
			for nominee in nominees:
				print("\t#" + str(ranking) + ":")
				
				if category.name in ['CompuMaster', 'CompuTeam', 'CompuAdoptado']:
					print("\t\tName: " + nominee.extra.replace("_", " "))
	
				elif category.name == 'CompuLove':
					print("\t\tName: " + get_full_name_from_entity(nominee.entity) + " & " + \
										 get_full_name_from_entity(nominee.entityOpt))
	
				elif category.name == 'CompuCartoon':
					print("\t\tName: " + get_full_name_from_entity(nominee.entity))
					print("\t\tCartoon: " + nominee.extra)
	
				else:
					print("\t\tName: " + get_full_name_from_entity(nominee.entity))
				
				print("\t\tNominations: " + str(nominee.nominations))
	
				ranking += 1
	
			print("")


if __name__ == "__main__":
    main()
