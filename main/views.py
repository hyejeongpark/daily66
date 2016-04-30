from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Habit
from .models import Log
from .forms import HabitForm, LogForm


def index(request):
    user_list = User.objects.all()
    habit_list = Habit.objects.all()
    return render(request, 'main/index.html',
                  {'user_list': user_list, 'habit_list': habit_list, })


def user_page(request, username):
    user = User.objects.get(username=username)
    habits = Habit.objects.filter(user=user)
    return render(request, 'main/user_page.html',
                  {'page_user': username, 'habits': habits, })


def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    logs = Log.objects.filter(habit=habit).order_by('date').reverse()
    return render(request, 'main/habit_detail.html',
                  {'habit': habit, 'logs': logs, })


@login_required
def habit_new(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(habit)
    else:
        form = HabitForm()
    return render(request, 'main/habit_form.html', {'form': form, })


def log_new(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save()
            return redirect(log.habit)
    else:
        form = LogForm()
    return render(request, 'main/log_form.html', {'form': form, })
