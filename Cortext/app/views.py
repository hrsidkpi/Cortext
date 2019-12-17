"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    username = ""
    type = -1
    if not 'userid' in request.session:
        return login(request)
    else:
        user = get_user(request.session["userid"])
        userid = user[0]
        username = user[1]
        type = user[2]

    if type == 1:
        classes = get_classes_teacher(userid)
        return render(request,
            'app/teacherhome.html',
            {
                'title':'Home Page',
                # 'year':datetime.now().year,
                'username':username,
                'type':type,
                'classes': classes
            })
    if type == 2:
        assignments = get_assignments_user(userid)
        return render(request,
            'app/studenthome.html',
            {
                'title':'Home Page',
                # 'year':datetime.now().year,
                'username':username,
                'type':type,
                'assignments': assignments,
            })

def studentassignment(request):
    assignmentid = request.POST['assignmentid']
    assignment = get_assignment(assignmentid)
    questions = get_questions_assignment(assignmentid)
    return render(request, 'app/studentassignment.html', {
        'assignment': assignment,
        'questions': questions
        })

def login(request):
    if 'user_id' in request.POST:
        success = attempt_login(request.POST['user_id'],request.POST['password'])
        if not success:
            return render(request, 'app/login.html', {
                    'error':'incorrect username or password'
                })
        request.session['userid'] = request.POST['user_id']
        return home(request)
    return render(request, 'app/login.html', {})

def register(request):
    if 'user_id' in request.POST:

        if user_exists(request.POST['user_id']):
            return render(request, 'app/register.html',{
                    'errorTxt': 'Username already exsists',
                })

        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        type = request.POST['type']
        password = request.POST['password']

        if type == '1':
            create_teacher(user_id, password, first_name, last_name)
        if type=='2':
            school = request.POST['school']
            create_student(user_id, password, first_name, last_name, school, -1)

        return HttpResponseRedirect("/login")

    return render(request, 'app/register.html',{})
    return None

def createassignment(request):
    return render(request, 'app/createassignment.html',{})

def teacherassignment(request):
    assignmentid = request.POST['assignmentid']
    assignment = get_assignment(assignmentid)
    questions = get_questions_assignment(assignmentid)
    submissions = get_submissions_assignment(assignmentid)
    return render(request, 'app/teacherassignment.html',{
            'assignment':assignment,
            'questions':questions,
            'submissions':submissions,
        })

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