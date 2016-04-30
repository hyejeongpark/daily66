from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Habit(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)

    def __str__(self):
        return "{} - {}".format(self.title, self.user.username)

    def get_absolute_url(self):
        return reverse('main:habit-detail', args=[self.pk])

class Log(models.Model):
    habit = models.ForeignKey(Habit)
    date = models.DateField()
    content = models.CharField(max_length=500)
    score = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.date, self.habit)
