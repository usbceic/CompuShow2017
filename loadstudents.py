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

from voting.library import *

def load():
	with open("computistas.txt", "r") as f:
		i = 0
		for line in f:
				student_id = line.split()[0]
				validate_and_register_user(student_id)
				print("ROW " + str(i))