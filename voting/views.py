#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  	  		 - Views file of the CompuSoft.  		#
#                                                   #
#####################################################

import json
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .library import *

##############################################
# Flag to enable voting modules (important!) #
##############################################
enable_voting = False                        #
##############################################

@login_required()
def index(request):
	students = get_students()
	return render(request, 'voting/index.html', {
		'home':True,
		'students':students,
		'enable_voting':enable_voting,
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
	
	categories  = get_categories()
	students    = get_students()
	nominations, categories_exist = get_nominations(request.user)

	return render(request, 'voting/nominate.html', {
		'nominations':True,
		'categories':categories,
		'students':students,
		'nominations':nominations,
		'categories_exist':categories_exist,
		'enable_voting':enable_voting,
	})

@login_required()
def vote(request):
	students = get_students()
	return render(request, 'voting/vote.html', {
		'enable_voting':enable_voting,
		'students':students,
	})

@login_required()
def log_out(request):
	logout(request)
	return HttpResponseRedirect('/login/')

@login_required()
def get_student_info(request):
	
	user = request.user
	category = request.GET.get('category')
	studentID = request.GET.get('studentID')
	studentID2 = request.GET.get('studentID2')
	comment = request.GET.get('comment')
	
	data = dict()
	data['category'] = category

	# Get student ID's
	studentID = get_student_id(studentID)

	# Student not found
	if studentID is None:
		data['not_found'] = True
		data['nominate'] = False
		data['already_nominated'] = False
		return HttpResponse(json.dumps(data))

	if studentID2 is not None:
		studentID2 = get_student_id(studentID2)
		if studentID2 is None:
			data['not_found_2'] = True
			data['nominate'] = False
			data['already_nominated'] = False
			return HttpResponse(json.dumps(data))

	# Check if not repeating nomination
	if already_nominated(user, category, studentID, studentID2):
		data['already_nominated'] = True
		data['nominate'] = False
		data['nom_id'], data['comment'] = get_nomination_info(user, category, studentID, studentID2)
		data['carnet']   = studentID
		data['carnet2']  = studentID2
		data['comment']  = comment

	# Then prepre for nomination
	else:
		# Get nomination info (user, category, studentID, studentID2, comment)
		data['nominate'] = True
		data['already_nominated'] = False
		data['comment']  = comment
		data['carnet']   = studentID
		data['carnet2']  = studentID2

	return HttpResponse(json.dumps(data))

@login_required()
def profile(request):
	
	######
	#from loadstudents import load
	#load()
	####### mmm

	students = get_students()

	nominations = []
	if enable_voting:
		nominations = get_nominations_profile(request.user.username)

	return render(request, 'voting/profile.html', {
		'profile':True,
		'student_name': get_full_name(request.user),
		'student_id': request.user.username,
		'students':students,
		'enable_voting':enable_voting,
		'my_profile':True,
		'nominations':nominations,
	})

@login_required()
def delete_nomination(request):

	user = request.user
	category = request.GET.get('category')
	studentID = request.GET.get('studentID')
	studentID2 = request.GET.get('studentID2')

	# Get student ID's
	studentID = get_student_id(studentID)

	if studentID2 is not None:
		studentID2 = get_student_id(studentID2)

	delete_nomination_db(user, category, studentID, studentID2)

	data = dict()

	data['nominee_entity'] = Student.objects.filter(student_id = studentID ).first().person.entity.pk
	
	if studentID2 is not None:
		data['nomineeOpt_entity'] = Student.objects.filter(student_id = studentID2).first().person.entity.pk
	else:
		data['nomineeOpt_entity'] = None

	return HttpResponse(json.dumps(data))

@login_required()
def make_nomination(request):

	if request.method == "POST":

		user = request.user
		category = request.POST.get('category')
		studentID = request.POST.get('studentID')
		studentID2 = request.POST.get('studentID2')
		comment = request.POST.get('comment')
		
		if not already_nominated(user, category, get_student_id(studentID), get_student_id(studentID2)):
			make_nomination_db(user, category, studentID, studentID2, comment)
	
		data = dict()

		data['nominee_entity'] = Student.objects.filter(student_id = get_student_id(studentID) ).first().person.entity.pk
		data['carnet'] = get_student_id(studentID)
		data['comment'] = comment

		if studentID2 is not None:
			data['nomineeOpt_entity'] = Student.objects.filter(student_id = get_student_id(studentID2) ).first().person.entity.pk
			data['carnet2'] = get_student_id(studentID2)
		else:
			data['nomineeOpt_entity'] = None
			data['carnet2'] = None

		return HttpResponse(json.dumps(data))

@login_required()
def view_profile(request):

	name = request.GET.get('search-bar')
	studentID = get_student_id(name)

	if studentID is None:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	students = get_students()

	nominations = []
	if enable_voting:
		nominations = get_nominations_profile(studentID)


	return render(request, 'voting/profile.html', {
		'profile':True,
		'student_name': name,
		'student_id': studentID,
		'students':students,
		'enable_voting':enable_voting,
		'my_profile':False,
		'nominations':nominations,
	})

@login_required()
def vote(request):

	students = get_students()
	nominees = get_nominees()
	return render(request, 'voting/vote.html', {
		'voting':True,
		'students':students,
		'enable_voting':enable_voting,
		'nominees':nominees,
	})