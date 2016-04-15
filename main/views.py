from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Habit

def index(request):
    user_list = User.objects.all()
    habit_list = Habit.objects.all()
    return render(request, 'main/index.html', {'user_list': user_list,'habit_list': habit_list,})

def habit_list(request, username):
    return render(request, 'main/index.html')
