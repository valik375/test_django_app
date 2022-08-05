from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from random import randint

from .forms import RegistrationForm, LoginForm
from .models import Game, Weapon, Hero, Monster


def index(request):
    if request.method == 'POST':
        game = Game()
        game.game_name = request.POST.get('name')
        game.game_logs = {"info_message": []}
        game.save()
        hero = Hero(health=100, level=1)
        hero.game = game
        hero.save()
        default_weapon = Weapon.objects.first()
        hero.weapon.add(default_weapon)
        monster = Monster(name='Oleg', health=60, level=1)
        monster.game = game
        monster.save()
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
    info = game.game_logs
    info_message = info["info_message"]
    hero = game.hero.get()
    monster = game.monster.get()
    monster_dialogs = ['На тобi КУРВА!', 'Отримуй!', 'Джета топ!', 'Получай!']
    info_message.append('--------------------------------------------')
    info_message.append(f'{monster.name} HP: {monster.health}')
    info_message.append(f'{request.user} HP: {hero.health}')
    info_message.append('--------------------------------------------')
    if request.GET.get('damage'):
        hero_damage = int(request.GET.get('damage'))
        monster_damage = monster.level * 10
        info_message.append(f'{request.user}: hit ({hero_damage} DMG)')

        if monster.health == 0:
            hero.level = hero.level + 1
            hero.health = 100 * hero.level
            monster.level = monster.level + 1
            monster.health = 50 * monster.level
        else:
            monster.health = monster.health - hero_damage
            info_message.append(f'{monster.name}: O KURWA!')
            if hero.health <= monster_damage:
                info_message.append('You Die!!!')
            else:
                info_message.append(f'{monster.name}: hit ({monster_damage} DMG)')
                info_message.append(f'{monster.name}: {monster_dialogs[int(randint(0, 3))]}')
                hero.health = hero.health - monster_damage

    game.game_logs = info
    game.save()
    hero.save()
    monster.save()

    return render(request, 'game_app/play.html', {
        'game': game,
        'hero': hero,
        'info_message': info_message
    })
