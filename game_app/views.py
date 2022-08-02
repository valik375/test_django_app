from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .game_assets.hero.hero_class import Hero
from .game_assets.weapon.weapons import Axe, Sword

from .forms import RegistrationForm, LoginForm
from .models import Game


def index(request):
    if request.method == 'POST':
        game = Game()
        game.user_name = request.POST.get('name')
        game.in_progress = True
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
    axe = Axe('Axe', 14, 20)
    hero = Hero(request.user, axe)
    attack_name = ''
    damage = ''
    info_message = ''
    for key in request.GET.keys():
        if key == 'damage':
            damage = request.GET.getlist(key)[0]
        elif key == 'name':
            attack_name = request.GET.getlist(key)[0]
        else:
            attack_id = request.GET.getlist(key)[0]
        info_message = f'Damaged by {attack_name} --- {damage} DMG '
    return render(request, 'game_app/play.html', {
        'game': game,
        'info_message': info_message,
        'hero': hero
    })
