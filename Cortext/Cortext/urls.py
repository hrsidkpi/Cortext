"""
Definition of urls for Cortext.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app.pages import home, login, register, teachersubmission, studentassignment, teacherassignment, createassignment
from pages import adminpage

urlpatterns = [
    path('', home.home, name='home'),
    path('home/', home.home, name='home'),
    path('login/', login.login, name='login'),
    path('login/submit/', login.submit, name='login_submit'),
    path('register/', register.register, name='register'),
    path('register/submit/', register.submit, name='register_submit'),
    path('logout/', login.logout, name='logout'),
    path('admin/', admin.site.urls),
    path('adminpage/', adminpage.admin, name='admin'),
    path('adminpage/submit/', adminpage.submit, name='admin'),
	path('studentassignment/', studentassignment.studentassignment, name='studentassignment'),
	path('studentassignment/submit/', studentassignment.submit, name='studentassignment_submit'),
    path('createassignment/', createassignment.createassignment, name='createassignment'),
    path('createassignment/submit/', createassignment.submit, name='createassignment_submit'),
    path('teacherassignment/', teacherassignment.teacherassignment, name='teacherassignment'),
    path('teachersubmission/', teachersubmission.teachersubmission, name='teachersubmission'),
    path('teachersubmission/submit/', teachersubmission.submit, name='teachersubmission_submit'),

]
