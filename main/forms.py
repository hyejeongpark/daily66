from django import forms
from .models import Habit, Log

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = '__all__'

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'
