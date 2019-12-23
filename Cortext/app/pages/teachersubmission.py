from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *


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
        })
