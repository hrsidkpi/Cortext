from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *



def studentassignment(request):
    assignmentid = request.POST['assignmentid']
    assignment = get_assignment(assignmentid)
    questions = get_questions_assignment(assignmentid)
    return render(request, 'app/studentassignment.html', {
        'assignment': assignment,
        'questions': questions
        })
