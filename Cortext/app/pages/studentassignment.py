from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *
import app.pages.home as home


def studentassignment(request):
    set_request(request)

    assignmentid = request.POST['assignmentid']
    #submission = get_submission_student(assignmentid)
    assignment = get_assignment(assignmentid)
    questions = get_questions_assignment(assignmentid)

    submission = [0, None, ["a", "b"]]

    answers = []
    for i in range(len(submission[2])):
        answers.append([questions[i][0], questions[i][1], submission[2][i]])

    return render(request, 'app/studentassignment.html', {
        'assignment': assignment,
        'questions': questions,
        'username': get_current_user()[1],
        'answers': answers,
        'submitted': False
        })

def submit(request):
    set_request(request)

    id = request.POST['assignment_id']
    answers = request.POST['answers']
    create_submission(id, answers)

    return home.home(request)
