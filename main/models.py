from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)

class Log(models.Model):
    habit = models.ForeignKey(Habit)
    date = models.DateField()
    content = models.CharField(max_length=500)
    score = models.IntegerField()

