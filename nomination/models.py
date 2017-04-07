#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  	   - Models file of the nomination module.   	#
#                                                   #
#####################################################

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Entity(models.Model):
	# Handle photos later
	#profile_photo = models.ImageField(upload_to=something,max_length=200, null=True)
	#nominee_photo = models.ImageField(upload_to=something,max_length=200, null=True)
	#winner_photo = models.ImageField(upload_to=something,max_length=200, null=True)

	class Meta:
		db_table = 'entity'

class Person(models.Model):

	person_id = models.CharField(
		max_length=200,
		unique=True,
		null=True,
		validators=[RegexValidator(regex='^([0-9])+$')]
	)
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
	status = models.CharField(max_length=20, null=True)
	entity = models.OneToOneField(
		Entity,
		on_delete = models.CASCADE,
		related_name = 'person',
		null = True,
	)

	class Meta:
		db_table = 'person'

class Group(models.Model):

	name = models.CharField(max_length=200)
	description = models.TextField(null=True)
	entity = models.OneToOneField(
		Entity,
		on_delete = models.CASCADE,
		related_name = 'group',
		null = True,
	)

	class Meta:
		db_table = 'group'

class Student(models.Model):

	student_id = models.CharField(
		max_length=10,
		unique=True,
		null=True,
		validators=[RegexValidator(regex='^([0-9]){2}-([0-9]){5}$')]	
	)
	career = models.CharField(max_length=200)

	class Meta:
		db_table = 'student'