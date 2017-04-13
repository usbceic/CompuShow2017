#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  	  		 - Views file of the CompuSoft.  		#
#                                                   #
#####################################################


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .library import *

@login_required()
def index(request):
	return HttpResponse("COMPUSOFT: Under development...")


def login(request):
	if request.method == 'POST':

		form = LoginForm(request.POST)
		if form.is_valid():
			
			student_id = form.cleaned_data['student_id']
			password = form.cleaned_data['password']

			if not user_is_registered(student_id):
				result = validate_and_register_user(student_id)
				if result == 'id not found':
					# student id not found in ldap
					return render(request, 'voting/login.html', {'form':form, 'invalid':True, 'notfound':True})
					
				elif result == 'not computer science student':
					return render(request, 'voting/login.html', {'form':form, 'invalid':True, 'notcs':True})					

			if login_user(student_id, password):
				return HttpResponseRedirect('/admin/')
			else:
				return render(request, 'voting/login.html', {'form':form, 'invalid':True, 'invalidpasswd':True})

		else:
			return render(request, 'voting/login.html', {'form':form})

	else:
		form = LoginForm()
		return render(request, 'voting/login.html', {'form':form})