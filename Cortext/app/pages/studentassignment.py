from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *
import app.pages.home as home
from django.views.decorators.http import require_POST
from django.http import JsonResponse


def studentassignment(request):
    set_request(request)

    assignmentid = request.POST['assignmentid']
    assignment = get_assignment(assignmentid)
    submission = get_submission_student(assignmentid)
    questions = get_questions_assignment(assignmentid)

    answers = []
    for i in range(len(submission[2])):
        answers.append([questions[i][0], questions[i][1], submission[2][i]])

    return render(request, 'app/studentassignment.html', {
        'assignment': assignment,
        'questions': questions,
        'username': get_current_user()[1],
        'answers': answers,
        'submissionid': submission[0],
        'submitted': False
        })

def submit(request):
    set_request(request)

    submission_id = request.POST['submission_id']
    answers = request.POST.getlist('answers[]')
    change_answers(submission_id, answers)

    return home.home(request)
