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
			message = "Invalid ID e.g. 00-12345")],
	)

	password = forms.CharField(
		label = "Password",
		widget = forms.PasswordInput,
	)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['student_id'].widget.attrs.update({
			'id': 'inputID',
			'class': 'form-control',
			'placeholder': 'Carnet: xx-xxxxx',
			'autofocus': True,
			'required': True
		})
		self.fields['password'].widget.attrs.update({
			'id': 'inputPassword',
			'class': 'form-control',
			'placeholder': 'Contraseña: cédula',
			'required': True
		})