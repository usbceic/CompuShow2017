#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  			    - Library of functions.  			#
#                                                   #
#####################################################

import ldap3
from .models import Entity, Person, Student
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Checks if student is registered in CompuSoft database
def user_is_registered(student_id):
	return Student.objects.filter(student_id = student_id).exists()

# Validate student in LDAP of USB and register in database
def validate_and_register_user(student_id):
	
	server = ldap3.Server('ldap.usb.ve', get_info=ldap3.ALL)
	conn = ldap3.Connection(server, auto_bind=True)
	conn.search('ou=People,dc=usb,dc=ve','(uid=%s)' % student_id, attributes=['uid','givenName','sn','personalId','mail','career'])
	
	if conn.entries:
		entry = conn.entries[0]
		if entry.career == 'Ingenieria de Computacion':
			register_user(entry)
			return 'successful registration'
		else:
			return 'not computer science student'
	else:
		return 'id not found'

# Register student in CompuSoft database
def register_user(entry):
	entity = Entity.objects.create(
		profile_photo = 'defaultProfilePhoto.jpg'
	)
	person = Person.objects.create(
		ci = str(entry.personalId),
		name = str(entry.givenName),
		surname = str(entry.sn),
		email = str(entry.mail),
		status = 'student',
		entity = entity,
	)
	user = User.objects.create_user(
		username = str(entry.uid),
		email = str(entry.mail),
		password = str(entry.personalId),
	)
	# Keep only first name
	user.first_name = str(entry.givenName).split()[0]
	user.last_name = str(entry.sn)
	user.save()	
	student = Student.objects.create(
		student_id = str(entry.uid),
		career = str(entry.career),
		person = person,
		user = user,
	)

# Get filename of user profile image
def get_user_image(user):
	student = user.student
	person = student.person
	entity = person.entity
	return str(entity.profile_photo)