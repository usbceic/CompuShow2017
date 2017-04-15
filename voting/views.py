#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  	  		 - Views file of the CompuSoft.  		#
#                                                   #
#####################################################


from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .library import *

@login_required()
def index(request):
	return render(request, 'voting/index.html', {
		'home':True,
	})

def log_in(request):

	# Redirect if user already logged in
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

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

			user = authenticate(username=student_id, password=password)
			
			if user is not None:
				login(request, user)
				request.session['profileimage'] = '/voting/images/profilePhotos/' + get_user_image(user)
				return HttpResponseRedirect('/')
			
			else:
				return render(request, 'voting/login.html', {'form':form, 'invalid':True, 'invalidpasswd':True})

		else:
			return render(request, 'voting/login.html', {'form':form})

	else:
		form = LoginForm()
		return render(request, 'voting/login.html', {'form':form})

@login_required()
def nominate(request):
	
	categories = get_categories()

	return render(request, 'voting/nominate.html', {
		'nominations':True,
		'categories':categories,
	})

@login_required()
def vote(request):
	return render(request, 'voting/vote.html', {
		'voting':True,
	})

@login_required()
def my_votes(request):
	return render(request, 'voting/my_votes.html', {
		'voting':True,
	})

@login_required()
def log_out(request):
	logout(request)
	return HttpResponseRedirect('/login/')