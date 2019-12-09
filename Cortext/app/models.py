"""
Definition of models.
"""

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    id = models.CharField(max_length=9, primary_key=True)
    first_name = models.CharField()
    last_name = models.CharField()


# Create your models here.
class Student(User):
    age_group = models.IntegerField()  # student's class
    school = models.ForeignKey('School', models.CASCADE)

    def __str__(self):
        return self.first_name, self.last_name


class School(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()

    def __str__(self):
        return self.name
