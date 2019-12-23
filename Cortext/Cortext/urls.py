"""
Definition of urls for Cortext.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from pages import home, login, register, teachersubmission, studentassignment, teacherassignment, createassignment


urlpatterns = [
    path('', home.home, name='home'),
    path('home/', home.home, name='home'),
    path('login/', login.login, name='login'),
    path('login/submit/', login.submit, name='login_submit'),
    path('register/', register.register, name='register'),
    path('register/submit/', register.submit, name='register_submit'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
	path('studentassignment/', studentassignment.studentassignment, name='studentassignment'),
    path('createassignment/', createassignment.createassignment, name='createassignment'),
    path('teacherassignment/', teacherassignment.teacherassignment, name='teacherassignment'),
    path('teachersubmission/', teachersubmission.teachersubmission, name='teachersubmission'),

]
