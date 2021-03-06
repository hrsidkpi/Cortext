"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *

import app.pages.home as home


def login(request):
    set_request(request)

    return render(request, 'app/login.html', {})

def submit(request):
    set_request(request)

    success = attempt_login(request.POST['user_id'],request.POST['password'])
    if not success:
        return render(request, 'app/login.html', {
                'error':'incorrect username or password'
            })
    return home.home(request)

def logout(request):
    set_request(request)

    logout_current_user()
    return render(request, 'app/login.html', {})
