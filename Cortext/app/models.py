"""
Definition of models.
"""
import datetime

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    id = models.CharField(max_length=9, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name, self.last_name

# Create your models here.
class Student(User):
    age_group = models.IntegerField()  # student's class
    school = models.ForeignKey('School', models.CASCADE)


class School(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Teacher(User):
    pass


class Question(models.Model):
    assignment_id = models.IntegerField()
    content = models.CharField(max_length=20)


class Submission(models.Model):
    student_id = models.CharField(max_length=9)
    teacher_id = models.CharField(max_length=9)
    content = models.CharField(max_length=20)
    assignment_id = models.IntegerField()
    grade = models.IntegerField(max_length=3)


class teacher_class(models.Model):
    teacher_id = models.CharField(max_length=9)
    school_id = models.CharField(max_length=6)


class teacher_student(models.Model):
    teacher_id = models.CharField(max_length=9)
    student_id = models.CharField(max_length=9)


class files(models.Model):
    path = models.CharField(max_length=255)
    question_id = models.IntegerField(max_length=3)


class class_student(models.Model):
    class_id = models.CharField(max_length=9)
    student_id = models.CharField(max_length=9)

class assignments(models.Model):
    assignment_id = models.CharField(max_length=9)
    teacher_id = models.CharField(max_length=9)
    description = models.CharField(max_length=255)
    subject = models.CharField(max_length=40)


class assignment_class(models.Model):
    assignment_id = models.CharField(max_length=9)
    class_id = models.CharField(max_length=9)
    submission_date = models.DateField(default=datetime.date.today())

class messages(models.Model):
    addressed_id = models.CharField(max_length=9)
    addressee_id = models.CharField(max_length=9)
    date = models.DateField(default=datetime.date.today())
    message_content = models.CharField(max_length=255)



