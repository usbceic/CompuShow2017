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

class Entity(models.Model):
	# Handle photos later
	#profile_photo = models.ImageField(upload_to=something,max_length=200, null=True)
	#nominee_photo = models.ImageField(upload_to=something,max_length=200, null=True)
	#winner_photo = models.ImageField(upload_to=something,max_length=200, null=True)

	class Meta:
		db_table = 'entity'

class Person(models.Model):

	ssn = models.CharField(max_length=200, unique=True, null=True)
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
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