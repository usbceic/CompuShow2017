#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  	  		 - Models file of Compusoft. 		  	#
#                                                   #
#####################################################

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Entity(models.Model):

	profile_photo = models.ImageField(upload_to='profilePhotos/',max_length=200, null=True)
	#nominee_photo = models.ImageField(upload_to=something,max_length=200, null=True)
	#winner_photo = models.ImageField(upload_to=something,max_length=200, null=True)

	def __str__(self):
		return str(self.id)

	class Meta:
		db_table = 'entity'
		verbose_name = "Entity"
		verbose_name_plural = "Entities"


class Person(models.Model):

	ci = models.CharField(
		max_length=200,
		unique=True,
		null=True,
		validators=[RegexValidator(regex='^([0-9])+$')]
	)
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	email = models.EmailField(unique=True, null=True)
	status = models.CharField(max_length=20, null=True)
	entity = models.OneToOneField(
		Entity,
		on_delete = models.CASCADE,
		related_name = 'person',
		null = True,
	)

	def __str__(self):
		return str(self.ci)

	class Meta:
		db_table = 'person'
		verbose_name = "Person"
		verbose_name_plural = "People"


class Group(models.Model):

	name = models.CharField(max_length=200)
	description = models.TextField(null=True)
	entity = models.OneToOneField(
		Entity,
		on_delete = models.CASCADE,
		related_name = 'group',
		null = True,
	)

	def __str__(self):
		return str(self.name)

	class Meta:
		db_table = 'group'
		verbose_name = "Group"
		verbose_name_plural = "Groups"


class Student(models.Model):

	student_id = models.CharField(
		max_length=10,
		unique=True,
		null=True,
		validators=[RegexValidator(regex='^([0-9]){2}-([0-9]){5}$')]
	)
	career = models.CharField(max_length=200)
	person = models.OneToOneField(
		Person,
		on_delete = models.CASCADE,
		related_name = 'student',
		null = True,
	)
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE,
		related_name = 'student',
		null = True,
	)

	def __str__(self):
		return str(self.student_id)

	class Meta:
		db_table = 'student'
		verbose_name = "Student"
		verbose_name_plural = "Students"


class Category(models.Model):

	name = models.CharField(max_length=200)
	description = models.TextField(null=True)
	image = models.ImageField(upload_to='categoryImages/',max_length=200, null=True)

	class Meta:
		db_table = 'category'
		verbose_name = "Category"
		verbose_name_plural = "Categories"


class Nominate(models.Model):

	datetime = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	comment = models.TextField(null=True)
	nominator = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE,
		null=True,
	)
	nominee = models.ForeignKey(
		Entity,
		on_delete = models.CASCADE,
		null=True,
		related_name = '+',
	)
	nomineeOpt = models.ForeignKey(
		Entity,
		on_delete = models.CASCADE,
		null=True,
		related_name = '+',
	)
	category = models.ForeignKey(
		Category,
		on_delete = models.CASCADE,
		null=True,
	)
	extra = models.TextField(null=True)

	def __str__(self):
		return str(self.id)

	class Meta:
		db_table = 'nominate'
		verbose_name = "Nomination"
		verbose_name_plural = "Nominations"


class Nominee(models.Model):

	votes = models.IntegerField(default=0)
	nominations = models.IntegerField(default=0)
	entity = models.ForeignKey(
		Entity,
		on_delete = models.CASCADE,
		null=True,
		related_name ='entity',
	)
	category = models.ForeignKey(
		Category,
		on_delete = models.CASCADE,
		null=True,
	)
	entityOpt = models.ForeignKey(
		Entity,
		on_delete = models.CASCADE,
		null=True,
		related_name ='entityOpt',
	)
	extra = models.TextField(null=True)

	def __str__(self):
		return str(self.id)

	class Meta:
		db_table = 'nominee'
		verbose_name = "Nominee"
		verbose_name_plural = "Nominees"


class Winner(models.Model):

	votes = models.IntegerField(default=0)
	entity = models.ForeignKey(
		Entity,
		on_delete = models.CASCADE,
		null=True,
	)
	category = models.ForeignKey(
		Category,
		on_delete = models.CASCADE,
		null=True,
	)	

	def __str__(self):
		return str(self.id)

	class Meta:
		db_table = 'winner'
		verbose_name = "Winner"
		verbose_name_plural = "Winners"
		unique_together = ('entity','category')
