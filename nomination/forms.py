#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  	  				Forms file.  					#
#                                                   #
#####################################################

from django import forms
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
	student_id = forms.CharField(
		label = "ID",
		strip = True,
		validators = [RegexValidator(
			regex = '^([0-9]){2}-([0-9]){5}$',
			message = "Invalid ID. XX-XXXXX")],
	)

	password = forms.CharField(
		label = "Password",
		widget = forms.PasswordInput,
	)