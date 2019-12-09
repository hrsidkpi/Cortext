"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Student(models.Model):

    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    type = models.IntegerField(default=0)

    ordering = ['username']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.username
class School(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()

    def __str__(self):
        return self.name