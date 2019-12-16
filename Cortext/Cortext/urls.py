"""
Definition of urls for Cortext.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
	path('studentassignment/', views.studentassignment, name='studentassignment'),
    path('createassignment/', views.createassignment, name='createassignment'),
    path('teacherassignment/', views.teacherassignment, name='teacherassignment'),
    path('teachersubmission/', views.teachersubmission, name='teachersubmission'),

]
