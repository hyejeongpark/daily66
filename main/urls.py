from django.conf.urls import url
from django.contrib.auth import views as auth_views
from main.forms import LoginForm
from main.views import HabitCreate, LogCreate, HabitUpdate
import main.views

urlpatterns = [
    url(r'^$', main.views.index, name="index"),
    url(r'^@(?P<username>[\w-]+)/$', main.views.user_page, name="user-page"),
    url(r'^habit/(?P<pk>\d+)/$', main.views.habit_detail,
        name="habit-detail"),
    url(r'^habit/add/$', HabitCreate.as_view(), name="habit-add"),
    url(r'^habit/(?P<pk>[0-9]+)/edit/$', HabitUpdate.as_view(),
        name="habit-edit"),
    url(r'^log/(?P<pk>\d+)/add/$', LogCreate.as_view(), name="log-add"),
    url(r'^accounts/join/$', main.views.join_view, name='join'),
    url(r'^accounts/login/$', auth_views.login,
        {'template_name': 'main/login.html',
         'authentication_form': LoginForm}, name='login'),
    url(r'^accounts/logout/$', main.views.logout_view, name="logout"),
]
