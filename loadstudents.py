#!/usr/bin/python3
#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  			    - Register students.    			#
#                                                   #
#####################################################

import os
import sys
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'compusoft.settings'
django.setup()

from voting.library import validate_and_register_user

with open("computistas.txt", "r") as f:
	registrations = 0
	nr_students   = 369

	for line in f:
	
			student_id = line.split()[0]
			print("REGISTER: " + str(student_id))
	
			if validate_and_register_user(student_id, True) == 'successful registration':
				registrations += 1
				print("SUCCESSFUL " + str(registrations) + " FROM " + str(nr_students))
	
			else:
				print("ERROR: USER NOT REGISTERED")
				sys.exit()
	
	print("REGISTERED USER: " + str(registrations) + "/" + str(nr_students))