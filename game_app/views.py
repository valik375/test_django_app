from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .game_assets.hero_class import Hero
from .game_assets.weapons import Axe, Sword
from .game_assets.enemy import Monster
from .game_assets.dishes import Chicken, Bread
from .game_assets.shop import Shop

from random import randint

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


axe = Axe('Axe', 20, 15)
sword = Sword('Sword', 13, 10)
super_axe = Axe('Super Axe', 25, 35)
super_sword = Sword('Super Sword', 19, 22)

weapon_array = [dict(index=1, item=axe), dict(index=2, item=sword),
                dict(index=3, item=super_axe), dict(index=4, item=super_sword)]
info_message = []


def play(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    hero = Hero(request.user, axe)
    attack_name = ''
    damage = ''

    oleg_dialogs = ['На тобi КУРВА!', 'Отримуй!', 'Джета топ!', 'Получай!']
    oleg_crip = Monster(f'Oleg level: 1', 1, oleg_dialogs)

    info_message.append('--------------------------------------------')
    info_message.append(f'{oleg_crip.name} HP: {oleg_crip.hit_points}')
    info_message.append(f'{hero.name} HP: {hero.hit_points}')

    for key in request.GET.keys():
        if key == 'damage':
            damage = request.GET.getlist(key)[0]
        elif key == 'name':
            attack_name = request.GET.getlist(key)[0]
        else:
            attack_id = request.GET.getlist(key)[0]

    info_message.append(f'Damaged by {attack_name} --- {damage} DMG')
    if oleg_crip.hit_points == 0:
        hero.set_experience(oleg_crip.experience)
        hero.money += oleg_crip.money
    else:
        info_message.append(f'{oleg_crip.dialogs[int(randint(0, 3))]}')
        if hero.hit_points <= oleg_crip.damage:
            info_message.append('You Die')
        else:
            hero.change_hip_points(oleg_crip.damage)

    info_message.append('--------------------------------------------')
    return render(request, 'game_app/play.html', {
        'game': game,
        'info_message': info_message,
        'hero': hero
    })
