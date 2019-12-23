from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *

import app.pages.home as home

def createassignment(request):
    set_request(request)

    return render(request, 'app/createassignment.html',{
            'username':get_current_user[1]
        })

def submit(request):
    set_request(request)

    if request.POST['send'] == "Save":
        pass
    if request.POST['send'] == "Submit":
        create_assignment(request.POST['title'], request.POST['due_date'], request.POST['questions'])
    return home.home(request)
