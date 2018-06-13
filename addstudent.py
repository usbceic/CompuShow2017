#!/usr/bin/python3
#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#           - Register student.          #
#                                                   #
#####################################################

import os
import sys
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'compusoft.settings'
django.setup()

from voting.library import validate_and_register_user

student_id = sys.argv[1]
print("REGISTER: " + str(student_id))

if validate_and_register_user(student_id, True) == 'successful registration':
  print("SUCCESSFUL")
else:
  print("ERROR: USER NOT REGISTERED")
