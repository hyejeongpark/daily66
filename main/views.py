from django.shortcuts import render
from .models import Habit

def index(request):
    return render(request, 'main/index.html')

def habit_list(request, username):
    return render(request, 'main/index.html')
