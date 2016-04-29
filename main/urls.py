from django.conf.urls import url
import main.views

urlpatterns = [
    url(r'^$', main.views.index, name="index"),
    url(r'^@(?P<username>[\w-]+)/$', main.views.user_page, name="user-page"),
    url(r'^habits/(?P<pk>\d+)/$', main.views.habit_detail, name="habit-detail"),
    url(r'^new/$', main.views.habit_new, name="habit-new"),
]
