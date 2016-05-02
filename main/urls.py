from django.conf.urls import url
from django.contrib.auth import views as auth_views
from main.forms import LoginForm
from main.views import HabitCreate, LogCreate
import main.views

urlpatterns = [
    url(r'^$', main.views.index, name="index"),
    url(r'^@(?P<username>[\w-]+)/$', main.views.user_page, name="user-page"),
    url(r'^habits/(?P<pk>\d+)/$', main.views.habit_detail,
        name="habit-detail"),
    url(r'^add/habit/$', HabitCreate.as_view(), name="habit-new"),
    url(r'^add/log/(?P<pk>\d+)/$', LogCreate.as_view(), name="log-new"),
    url(r'^accounts/join/$', main.views.join_view, name='join'),
    url(r'^accounts/login/$', auth_views.login,
        {'template_name': 'main/login.html',
         'authentication_form': LoginForm}, name='login'),
    url(r'^accounts/logout/$', main.views.logout_view, name="logout"),
]
