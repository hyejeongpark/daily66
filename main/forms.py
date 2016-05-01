from django import forms
from .models import Habit, Log
from django.forms import extras
import datetime


class HabitForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': "form-control",
                                      'placeholder': "Title"}), )
    description = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control",
                                      'placeholder': "Description"}), )
    class Meta:
        model = Habit
        fields = ('title', )


class LogForm(forms.ModelForm):
    date = forms.DateField(
        initial=datetime.date.today,
        widget=extras.SelectDateWidget(years=[y for y in range(2010,2020)], ))
    content = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={'class': "form-control",
                                      'placeholder': "Content"}), )
    score = forms.IntegerField()
    class Meta:
        model = Log
        fields = ('date', 'content', 'score')
