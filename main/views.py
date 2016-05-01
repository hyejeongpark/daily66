from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from main.models import Habit, Log
from main.forms import HabitForm, LogForm, UserCreationForm

def join_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password1'])
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'main/join.html', {'form': form, })


def logout_view(request):
    logout(request)
    return redirect('main:index')


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
    logs = Log.objects.filter(habit=habit).order_by('-date')
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


@login_required
def log_new(request, pk):
    habit = Habit.objects.get(pk=pk)
    if request.user != habit.user:
        return redirect(habit)

    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.habit = habit
            log.save()
            return redirect(log.habit)
    else:
        form = LogForm()
    return render(request, 'main/log_form.html', {'form': form, })
