from django.contrib import admin
from .models import Habit
from .models import Log

admin.site.register(Habit)
admin.site.register(Log)
