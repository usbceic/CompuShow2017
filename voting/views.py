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
from random import shuffle
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User, update_last_login
from django.core.mail import EmailMessage

from pprint import pprint
from .forms import LoginForm
from .library import *

from .models import *
from django.core import serializers
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
		'safari': browser_safari(request.META['HTTP_USER_AGENT'])
	})

def log_in(request):

	# Redirect if user already logged in
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':

		if request.user.is_authenticated():
			return HttpResponseRedirect('/')

		form = LoginForm(request.POST)
		if form.is_valid():
			student_id = form.cleaned_data['student_id']
			password = form.cleaned_data['password']
			print(student_id)
			print(password)

			if not user_is_registered(student_id):
				print(student_id)
				print(password)
				result = validate_and_register_user(student_id)
				if result == 'id not found':
					# student id not found in ldap
					return render(request, 'voting/login.html', {'form':form, 'invalid':True, 'notfound':True})
					
				elif result == 'not computer science student':
					return render(request, 'voting/login.html', {'form':form, 'invalid':True, 'notcs':True})					
			print('aqui')
			user = authenticate(username=student_id, password=password)

			if user is not None:

				if account_activated(user):
					login(request, user)
					request.session['profileimage'] = '/voting/images/profilePhotos/' + get_user_image(user) + '.jpg'
				else:
					account_activation_email(request, user)
					return render(request, 'voting/login.html', {'form':form, 'not_activated':True})

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
	categories = [categories[0:6], categories[6:12], categories[12:]]
	return render(request, 'voting/nominate.html', {
		'nominate':True,
		'categories':categories,
		'students':students,
		'nominations':nominations,
		'categories_exist':categories_exist,
		'enable_voting':enable_voting,
		'safari': browser_safari(request.META['HTTP_USER_AGENT'])
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
	cartoon = request.GET.get('cartoon')
	print(user)
	data = dict()
	data['category'] = category

	# Get student ID's
	freeFieldCategories = ['CompuMaster', 'CompuAdoptado', 'CompuTeam']
	if category not in freeFieldCategories:
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
		print(studentID)
		print(studentID2)
		data['already_nominated'] = True
		data['nominate'] = False
		data['nom_id'], data['comment'] = get_nomination_info(user, category, studentID, studentID2)
		
		if category not in freeFieldCategories:
			data['nominee_entity'] = Student.objects.filter(student_id = studentID ).first().person.entity.pk
		else:
			data['nominee_entity'] = studentID

		if category not in freeFieldCategories:
			data['carnet'] = studentID
		else:
			data['carnet'] = ""
		
		data['carnet2']  = studentID2
		data['comment']  = comment
		
		if category == 'CompuCartoon':
			data['cartoon']  = get_cartoon(user, studentID)
		
		if studentID2 is not None:
			data['nomineeOpt_entity'] = Student.objects.filter(student_id = studentID2).first().person.entity.pk

	# Then prepre for nomination
	else:
		# Get nomination info (user, category, studentID, studentID2, comment)
		data['nominate'] = True
		data['already_nominated'] = False
		data['comment']  = comment
		
		if category not in freeFieldCategories:
			data['carnet'] = studentID
		else:
			data['carnet'] = ""

		data['carnet2']  = studentID2
		data['cartoon']  = cartoon

	return HttpResponse(json.dumps(data))


@login_required()
def delete_nomination(request):

	user = request.user
	category = request.GET.get('category')
	studentID = request.GET.get('studentID')
	studentID2 = request.GET.get('studentID2')

	# Get student ID's
	freeFieldCategories = ['CompuMaster', 'CompuAdoptado', 'CompuTeam']
	if category not in freeFieldCategories:
		studentID = get_student_id(studentID)

	if studentID2 is not None:
		studentID2 = get_student_id(studentID2)

	delete_nomination_db(user, category, studentID, studentID2)

	data = dict()

	freeFieldCategories = ['CompuMaster', 'CompuAdoptado', 'CompuTeam']
	if category not in freeFieldCategories:
		data['nominee_entity'] = Student.objects.filter(student_id = studentID ).first().person.entity.pk
		
		if studentID2 is not None:
			data['nomineeOpt_entity'] = Student.objects.filter(student_id = studentID2).first().person.entity.pk
		else:
			data['nomineeOpt_entity'] = None

	else:
		data['nominee_entity'] = studentID
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
		cartoon = request.POST.get('cartoon')
		
		if not already_nominated(user, category, get_student_id(studentID), get_student_id(studentID2)):
			make_nomination_db(user, category, studentID, studentID2, comment, cartoon)
	
		data = dict()

		freeFieldCategories = ['CompuMaster', 'CompuAdoptado', 'CompuTeam']
		if category in freeFieldCategories:
			data['nominee_entity'] = studentID
			data['carnet'] = None
			data['comment'] = comment
			data['cartoon'] = None
			data['nomineeOpt_entity'] = None
			data['carnet2'] = None

		else:
			data['nominee_entity'] = Student.objects.filter(student_id = get_student_id(studentID) ).first().person.entity.pk
			data['carnet'] = get_student_id(studentID)
			data['comment'] = comment
			data['cartoon'] = cartoon
	
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
		'safari': browser_safari(request.META['HTTP_USER_AGENT'])
	})

@login_required()
def vote(request):

	user = request.user
	students = get_students()
	categories = get_categories()
	category = get_category(request.GET.get('category'))
	
	# Get nominees and shuffle (because they come already sorted)
	nominees, voted = get_nominees_from_category(category, user)
	shuffle(nominees)
	nominees_upper = nominees[:int((len(nominees)+1)/2)]
	nominees_lower = nominees[int((len(nominees)+1)/2):]

	return render(request, 'voting/vote.html', {
		'voting':True,
		'voted':voted,
		'students':students,
		'enable_voting':enable_voting,
		'category':category,
		'categories':categories,
		'nominees_upper':nominees_upper,
		'nominees_lower':nominees_lower,
		'nominees_count':len(nominees),
		'safari': browser_safari(request.META['HTTP_USER_AGENT']),
	})


@login_required()
def upd_pswd(request):

	user = request.user
	new_pswd = request.POST.get('new_pswd')
	
	upd_pswd_db(user, new_pswd)

	return HttpResponse(json.dumps(dict()))

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        update_last_login(None, user)
        return render(request, 'voting/registration_success.html')
    else:
        return render(request, 'voting/registration_success.html', {'invalid':True})

@login_required()
def get_vote_info(request):

	category = request.GET.get('category')
	studentID = request.GET.get('studentID')
	studentIDOpt = request.GET.get('studentIDOpt')
	extra = request.GET.get('extra')

	data = dict()
	data['comments'] = get_comments_from_nomination(category, studentID, studentIDOpt, extra)
	
	return HttpResponse(json.dumps(data))

@login_required()
def voting(request):

	user = request.user
	category = request.POST.get('category')
	studentID = request.POST.get('studentID')
	studentIDOpt = request.POST.get('studentIDOpt')
	extra = request.POST.get('extra')
	
	data = dict()

	if not already_voted(user, category):
		data['valid'] = True
		process_voting(user, studentID, studentIDOpt, category, extra)
	else:
		data['valid'] = False

	return HttpResponse(json.dumps(data))

## Función que retorna las categorías:
def categories(request):
	if request.method == 'GET':
		categories = Category.objects.all()
		return HttpResponse(serializers.serialize('json', categories), content_type='application/json')

def category(request):
	if request.method == 'GET':
		pk = request.GET.get('pk')
		cat = Category.objects.filter(pk=pk)
		return HttpResponse(serializers.serialize('json', cat), content_type='application/json')
