from django import forms
from .models import Habit, Log


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('title', )


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ('date', 'content', 'score')
