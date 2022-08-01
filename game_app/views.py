from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .forms import RegistrationForm, LoginForm
from .models import Game


def index(request):
    if request.method == 'POST' and request.POST.get('name'):
        game = Game()
        game.user_name = request.POST.get('name')
        game.status = True
        game.save()
        return redirect(f'/game_app/{game.pk}')
    else:
        return render(request, 'game_app/index.html', {
            'error_message': 'Please enter correct name!'
        })


def registration(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            User.objects.create_user(**registration_form.cleaned_data)
            return redirect('/game_app')
    else:
        registration_form = RegistrationForm()
        return render(request, 'game_app/registration.html', {'registration_form': registration_form})


def user_login(request):
    if request.method == 'POST':
        user_login_form = LoginForm(request.POST)
        if user_login_form.is_valid():
            user = authenticate(request, **user_login_form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/game_app')
            else:
                return render(request, 'game_app/login.html', {'user_login_form': user_login_form})
    else:
        user_login_form = LoginForm()
        return render(request, 'game_app/login.html', {'user_login_form': user_login_form})


def play(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game_app/play.html', {'game': game})
