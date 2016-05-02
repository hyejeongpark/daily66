from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext, ugettext_lazy as _
from main.models import Habit, Log
import datetime


alphanumeric = RegexValidator(
    r'^[0-9a-z]*$', 'Only alphanumeric(0-9a-z) characters are allowed.')


class UserCreationForm(forms.ModelForm):
    error_messages = {
        'duplicate_email': _("Email addresses must be unique."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control"}),
        validators=[alphanumeric])
    email = forms.CharField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': "form-control"}), )
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username", "email", )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email)\
                .exclude(username=username).count():
            raise forms.ValidationError(
                self.error_messages['duplicate_email'],
                code='duplicate_email',
            )
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control"}), )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': "form-control"}), )


class HabitForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': "form-control"}), )
    description = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"}), )
    class Meta:
        model = Habit
        fields = ('title', 'description')


class LogForm(forms.ModelForm):
    date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={'class': "form-control",
                                      'type': "date"}), )
    content = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={'class': "form-control"}), )
    score = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "form-control",
                                      'type': "number"}), )
    class Meta:
        model = Log
        fields = ('date', 'content', 'score')
