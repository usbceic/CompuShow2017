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

	if len(sys.argv) <= 1 or sys.argv[1][0] != '-':
		usage()
		sys.exit()

	queryType = sys.argv[1]
	if queryType == "-nomination":
		results = get_nominees(1000)
	elif queryType == "-vote":
		results = get_participants()
	else:
		usage()
		sys.exit()
	
	for category, nominees in results.items():

		# Specify categories to be displayed in the console
		if len(sys.argv) <= 2 or category.name in sys.argv[2:]:

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
					print("\t\tName: "    + get_full_name_from_entity(nominee.entity))
					print("\t\tCartoon: " + nominee.extra)
	
				else:
					print("\t\tName: "    + get_full_name_from_entity(nominee.entity))
				
				if queryType == "-nomination":
					print("\t\tNominations: " + str(nominee.nominations))
				else:
					print("\t\tVotes: " + str(nominee.votes))

				ranking += 1
	
			print("")

def usage():
	print("Usage:")
	print("getInfo.py [-nomination | -vote] [category_name]")

if __name__ == "__main__":
    main()
