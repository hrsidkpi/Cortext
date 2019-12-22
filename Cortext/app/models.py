"""
Definition of models.
"""
import datetime

from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    id = models.CharField(max_length=9, primary_key=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    age_group = models.IntegerField(default=-1)  # student's class
    school = models.ForeignKey('School', models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class School(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    id = models.CharField(max_length=9, primary_key=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    assignment_id = models.IntegerField(default=-1)
    content = models.TextField()


class Submission(models.Model):
    submission_id = models.IntegerField(primary_key=True)
    student_id = models.CharField(max_length=9)
    # teacher_id = models.CharField(max_length=9)
    assignment_id = models.IntegerField()
    grade = models.IntegerField(default=-1)


class Answers(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    submission_id = models.IntegerField()
    question_id = models.IntegerField()
    content = models.TextField()


class teacher_class(models.Model):
    teacher_id = models.CharField(max_length=9)
    school_id = models.CharField(max_length=6)


class teacher_student(models.Model):
    teacher_id = models.CharField(max_length=9)
    student_id = models.CharField(max_length=9)


class files(models.Model):
    path = models.CharField(max_length=255)
    question_id = models.IntegerField()


class class_student(models.Model):
    class_id = models.CharField(max_length=9)
    student_id = models.CharField(max_length=9)


class assignments(models.Model):
    assignment_id = models.IntegerField(primary_key=True)
    teacher_id = models.CharField(max_length=9)
    description = models.TextField()
    subject = models.CharField(max_length=40)
    due_date = models.DateTimeField(default=datetime.datetime.now, blank=True)



class assignment_class(models.Model):
    assignment_id = models.CharField(max_length=9)
    class_id = models.CharField(max_length=9)
    submission_date = models.DateField(default=datetime.date.today())


class messages(models.Model):
    addressed_id = models.CharField(max_length=9)
    addressee_id = models.CharField(max_length=9)
    date = models.DateField(default=datetime.date.today())
    message_content = models.CharField(max_length=255)
