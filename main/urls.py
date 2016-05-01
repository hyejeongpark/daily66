from django.conf.urls import url
from django.contrib.auth import views as auth_views
from main.forms import LoginForm
import main.views

urlpatterns = [
    url(r'^$', main.views.index, name="index"),
    url(r'^@(?P<username>[\w-]+)/$', main.views.user_page, name="user-page"),
    url(r'^habits/(?P<pk>\d+)/$', main.views.habit_detail,
        name="habit-detail"),
    url(r'^new/$', main.views.habit_new, name="habit-new"),
    url(r'^log/(?P<pk>\d+)/$', main.views.log_new, name="log-new"),
    url(r'^accounts/join/$', main.views.join_view, name='join'),
    url(r'^accounts/login/$', auth_views.login,
        {'template_name': 'main/login.html',
         'authentication_form': LoginForm}, name='login'),
    url(r'^accounts/logout/$', main.views.logout_view, name="logout"),
]
