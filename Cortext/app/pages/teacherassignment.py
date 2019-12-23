from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *

def teacherassignment(request):
    current_request = request

    assignmentid = request.POST['assignmentid']
    assignment = get_assignment(assignmentid)
    questions = get_questions_assignment(assignmentid)
    submissions = get_submissions_assignment(assignmentid)
    return render(request, 'app/teacherassignment.html',{
            'assignment':assignment,
            'questions':questions,
            'submissions':submissions,
            'username':get_current_user()[1]
        })