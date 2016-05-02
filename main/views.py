from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
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


@method_decorator(login_required, name='dispatch')
class HabitCreate(CreateView):
    form_class = HabitForm
    template_name = 'main/habit_form.html'

    def form_valid(self, form):
        habit = form.save(commit=False)
        habit.user = self.request.user
        habit.save()
        return redirect(habit)


@method_decorator(login_required, name='dispatch')
class LogCreate(CreateView):
    model = Log
    form_class = LogForm
    template_name = 'main/log_form.html'

        # if self.request.user != habit.user:
        #     return redirect(habit)

    def form_valid(self, form):
        habit = Habit.objects.get(pk=self.kwargs['pk'])
        log = form.save(commit=False)
        log.habit = habit
        log.save()
        return redirect(log.habit)
