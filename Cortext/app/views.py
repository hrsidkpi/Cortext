"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect

from .models import Student


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    username = ""
    type = -1
    if 'username' in request.session:
        user = Student.objects.filter(username=request.session["username"])[0]
        username = user.username
        type = user.type
    return render(request,
                  'app/index.html',
                  {
                      'title': 'Home Page',
                      'year': datetime.now().year,
                      'username': username,
                      'type': type,
                  })


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,
                  'app/contact.html',
                  {
                      'title': 'Contact',
                      'message': 'Your contact page.',
                      'year': datetime.now().year,
                  })


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(request,
                  'app/about.html',
                  {
                      'title': 'About',
                      'message': 'Your application description page.',
                      'year': datetime.now().year,
                  })





def login(request):
    if 'username' in request.POST:
        obj = Student.objects.filter(username=request.POST['username'], password=request.POST['password'])
        if len(obj) == 0:
            return render(request, 'app/login.html', {
                'error': 'incorrect username or password'
            })
        request.session['username'] = obj[0].username
        return home(request)
    return render(request, 'app/login.html', {})


def register(request):
    if 'username' in request.POST:

        obj = Student.objects.filter(username=request.POST['username'])
        if len(obj) > 0:
            return render(request, 'app/register.html', {
                'errorTxt': 'Username already exsists',
            })

        s = Student.objects.create(username=request.POST['username'], password=request.POST['password'],
                                   type=request.POST['type'])
        s.save()
        return HttpResponseRedirect("/login")

    return render(request, 'app/register.html', {})
