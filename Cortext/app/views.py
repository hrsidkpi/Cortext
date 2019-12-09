"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from APIs import *


from .models import Student

def home(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	username = ""
	type = -1
	if 'userid' in request.session:
		user = Student.objects.filter(username = request.session["username"])[0]
		username = user.username
		type = user.type
		assignments = get_assignments_user(user.id)
		print(type)
	else:
		return login(request)
	if type == 1:
		return render(request,
			'app/teacherthome.html',
			{
				'title':'Home Page',
				'year':datetime.now().year,
				'username':username,
				'type':type,
			})
	if type == 0:
		return render(request,
			'app/studenthome.html',
			{
				'title':'Home Page',
				'year':datetime.now().year,
				'username':username,
				'type':type,
				'assignments': assignments,
			})

def studentassignment(request):
	assignmentid = request.GET['assignmentid']
	return render(request, 'app/studentassignment.html', {
		'assignmentid': assignmentid
		})
	
def login(request):
	if 'user_id' in request.POST:
		success = attempt_login(request.POST['user_id'],request.POST['password'])
		if not success:
			return render(request, 'app/login.html', {
					'error':'incorrect username or password'
				})
		request.session['userid'] = request.POST['user_id']
		return home(request)
	return render(request, 'app/login.html', {})

def register(request):

	if 'user_id' in request.POST:

		obj = Student.objects.filter(username=request.POST['username'])
		if len(obj) > 0:
			return render(request, 'app/register.html',{
					'errorTxt': 'Username already exsists',
				})

		s = Student.objects.create(username=request.POST['username'], password=request.POST['password'], type=request.POST['type'])
		s.save()
		return HttpResponseRedirect("/login")

	return render(request, 'app/register.html',{})
