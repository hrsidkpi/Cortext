from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *
import pages.home as home
from django.views.decorators.http import require_POST
from django.http import JsonResponse


def teachersubmission(request):
    submissionid = request.POST['submissionid']
    assignment = get_assignment_submission(submissionid)
    questions = get_questions_assignment(assignment[0])
    submission = get_submission(submissionid)

    answers = []
    for i in range(len(submission[3])):
        answers.append([questions[i][0], questions[i][1], submission[3][i]])

    return render(request, 'app/teachersubmission.html', {
            'assignment': assignment,
            'submission': submission,
            'questions': questions,
            'answers': answers,
            'username':get_current_user()[1]
        })


def submit(request):
    submission = request.POST['submission_id']
    answers = request.POST.getlist('answers[]')
    change_answers(submission, answers)
    return home.home(request)