from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Habit
from .models import Log

def index(request):
    user_list = User.objects.all()
    habit_list = Habit.objects.all()
    return render(request, 'main/index.html', {'user_list': user_list,'habit_list': habit_list,})

def user_page(request, username):
    user = User.objects.get(username=username)
    habits = Habit.objects.filter(user=user)
    return render(request, 'main/user_page.html', {'user': username, 'habits': habits,})

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    logs = Log.objects.filter(habit=habit)
    return render(request, 'main/habit_detail.html', {'habit': habit, 'logs': logs,})
