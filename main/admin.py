from django.contrib import admin
from .models import Habit
from .models import Log


class HabitAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


class LogAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date')

admin.site.register(Habit, HabitAdmin)
admin.site.register(Log, LogAdmin)
