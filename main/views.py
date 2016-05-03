from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
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
class HabitUpdate(UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = 'main/habit_form.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect(obj)
        return super(HabitUpdate, self).dispatch(request, *args, **kwargs)

    def form_vaild(self, form):
        habit = Habit.objects.get(pk=self.object.pk)
        is_updated = form.cleaned_data['title'] != habit.title or \
            form.cleaned_data['description'] != habit.description
        if is_updated:
            habit = form.save()
            args = (habit.user.username, habit.pk)
            url = reverse('main:habit-detail', args=args)
        else:
            args = (self.object.user.username, self.object.id)
            url = reverse('main:habit-detail', args=args)
        return HttpResponseRedirect(url)


@method_decorator(login_required, name='dispatch')
class HabitDelete(DeleteView):
    model = Habit
    template_name = 'main/habit_delete_confirm.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect(obj)
        return super(HabitDelete, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('main:user-page',
                            kwargs={'username': self.request.user.username})

    def delete(self, request, *args, **kwargs):
        return super(HabitDelete, self).delete(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class LogCreate(CreateView):
    form_class = LogForm
    template_name = 'main/log_form.html'

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Habit, pk=self.kwargs.get('pk'))
        if obj.user != self.request.user:
            return redirect(obj)
        return super(LogCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        habit = get_object_or_404(Habit, pk=self.kwargs.get('pk'))
        log = form.save(commit=False)
        log.habit = habit
        log.save()
        return redirect(log.habit)


@method_decorator(login_required, name='dispatch')
class LogUpdate(UpdateView):
    model = Log
    form_class = LogForm
    template_name = 'main/log_form.html'

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Log, pk=self.kwargs.get('pk'))
        print(obj.habit)
        if obj.habit.user != self.request.user:
            return redirect(obj)
        return super(LogUpdate, self).dispatch(request, *args, **kwargs)

    def form_vaild(self, form):
        log = Log.objects.get(pk=self.object.pk)
        is_updated = form.cleaned_data['date'] != log.date or \
            form.cleaned_data['content'] != log.content or \
            form.cleaned_date['score'] != log.score
        if is_updated:
            log = form.save()
            args = (log.habit.user.username, log.habit.pk)
            url = reverse('main:habit-detail', args=args)
        else:
            args = (self.object.habit.user.username, self.object.habit.id)
            url = reverse('main:habit-detail', args=args)
        return HttpResponseRedirect(url)
