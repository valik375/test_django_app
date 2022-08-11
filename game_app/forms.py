from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Game


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=225, required=True)
    email = forms.EmailField(max_length=225, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")


class LoginForm(forms.Form):
    # AuthenticationForm
    username = forms.CharField(max_length=225, required=True)
    password = forms.CharField(max_length=225, widget=forms.PasswordInput, label="Password", required=True)


class CreateGameForm(forms.ModelForm):
    game_name = forms.CharField(max_length=225, label="Game name", required=True)

    class Meta:
        model = Game
        fields = ['game_name']


class EditGame(forms.ModelForm):
    game_name = forms.CharField(max_length=225, label="New game name", required=True)

    class Meta:
        model = Game
        fields = ['game_name']
