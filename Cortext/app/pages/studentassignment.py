from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *
import app.pages.home as home


def studentassignment(request):
    set_request(request)

    assignmentid = request.POST['assignmentid']
    assignment = get_assignment(assignmentid)
    questions = get_questions_assignment(assignmentid)
    return render(request, 'app/studentassignment.html', {
        'assignment': assignment,
        'questions': questions,
        'username': get_current_user()[1]
        })

def submit(request):
    set_request(request)

    id = request.POST['assignment_id']
    answers = request.POST['answers']
    create_submission(id, answers)

    return home.home(request)
