from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *
from django.views.decorators.http import require_POST
from django.http import JsonResponse

import app.pages.home as home

def admin(request):
    user = get_current_user()
    teachers = get_teachers_school(user[3])
    return render(request, 'app/admin.html', {
            'teachers': teachers
        })

def submit(request):
    user = get_current_user()
    ids = request.POST['ids']
    names = request.POST['names']
    passwords = request.POST['passwords']
    
    teachers = []
    for i in range(len(ids)):
        if passwords[i] != '':
            teachers.append([ids[i], names[i], passwords[i]])
        else:
            teachers.append([ids[i], names[i]])

    set_teachers_school(user[3], teachers)

