from django import forms
from .models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=225)
    first_name = forms.CharField(max_length=225)
    last_name = forms.CharField(max_length=225)
    email = forms.CharField(max_length=225)
    password = forms.CharField(max_length=225, widget=forms.PasswordInput, label="Password")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=225)
    password = forms.CharField(max_length=225, widget=forms.PasswordInput, label="Password")
