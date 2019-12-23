"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *

import app.pages.login as login

def home(request):
    request.session['username'] = None
    set_request(request)

    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    username = ""
    type = -1

    if not is_connected():
        return login.login(request)

    user = get_current_user()
    type = user[2]

    if type == 1:
        return teacher_home(request, user)
    if type == 2:
        return student_home(request, user)

def teacher_home(request, user):
    set_request(request)

    classes = get_classes_teacher(user[0])
    return render(request,
        'app/teacherhome.html',
        {
            'title':'Home Page',
            # 'year':datetime.now().year,
            'username':user[1],
            'classes': classes
        })

def student_home(request, user):
    set_request(request)

    assignments = get_assignments_user(user[0])
    return render(request,
        'app/studenthome.html',
        {
            'title':'Home Page',
            # 'year':datetime.now().year,
            'username':user[1],
            'assignments': assignments,
        })