from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    title           = models.CharField(max_length=60, blank=True)
    user            = models.ForeignKey(User, default=True, on_delete = models.CASCADE)

class Assignment(models.Model):
    title           = models.CharField(max_length=60, blank=True)
    description     = models.CharField(max_length=120, blank=True)
    due             = models.DateField(blank=True)
    project         = models.ForeignKey(Project, default=True, on_delete = models.CASCADE)

class Reminder(models.Model):
    description          = models.CharField(max_length=120, blank=True)
    project         = models.ForeignKey(Project, default=True, on_delete = models.CASCADE)
