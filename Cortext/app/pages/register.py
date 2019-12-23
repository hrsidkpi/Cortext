"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *

import app.pages.login as login

def register(request):
    set_request(request)

    return render(request, 'app/register.html',{})

def submit(request):
    set_request(request)

    if user_exists(request.POST['user_id']):
        return render(request, 'app/register.html',{
                'errorTxt': 'Username already exsists',
            })

    user_id = request.POST['user_id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    type = request.POST['type']
    password = request.POST['password']

    if type == '1':
        create_teacher(user_id, password, first_name, last_name)
    if type=='2':
        school = request.POST['school']
        create_student(user_id, password, first_name, last_name, school, -1)

    return login.login(request)