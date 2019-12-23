from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.APIs import *

def createassignment(request):
    return render(request, 'app/createassignment.html',{})
