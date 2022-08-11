from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from random import randint

from .decorators import is_owner
from .forms import RegistrationForm, LoginForm, CreateGameForm, EditGame
from .models import Game, Weapon, Hero, Monster, Skills


@login_required(login_url='/game_app/login')
def index(request):
    if request.method == 'POST':
        create_game_form = CreateGameForm(request.POST)
        if create_game_form.is_valid():
            game = Game()
            game.game_name = create_game_form.cleaned_data['game_name']
            game.game_logs = {"info_message": []}
            game.user_id = request.user.pk
            game.save()

            hero = Hero()
            hero.game = game
            if not Weapon.objects.first():
                hero.weapon = Weapon(name='Axe', damage=20)
            else:
                hero.weapon = Weapon.objects.get(name='Axe')

            if not Skills.objects.first():
                hero.skills = Skills(name='Бред', damage=20)
            else:
                hero.skills = Skills.objects.get(name='Бред')

            hero.save()

            monster = Monster(name='Oleg')
            monster.game = game
            monster.save()
            return redirect(f'/game_app/{game.pk}')
    else:
        create_game_form = CreateGameForm()
        return render(request, 'game_app/index.html', {'create_game_form': create_game_form})


@login_required(login_url='/game_app/login')
def games_list(request):
    games = Game.objects.filter(user_id=request.user.pk)
    if len(games) != 0:
        return render(request, 'game_app/games_list.html', {
            'games_list': games
        })
    else:
        return render(request, 'game_app/games_list.html', {
            'message': 'You have no games'
        })


@login_required(login_url='/game_app/login')
def delete_game(request, game_id):
    deleted_game = get_object_or_404(Game, pk=game_id)
    deleted_game.delete()
    return redirect('/game_app/games_list')


@login_required(login_url='/game_app/login')
def edit_game(request, game_id):
    if request.method == 'POST':
        print(request.POST)
        edited_game = get_object_or_404(Game, pk=game_id)
        edit_game_form = EditGame(request.POST)
        if edit_game_form.is_valid():
            edited_game.game_name = edit_game_form.cleaned_data['game_name']
            edited_game.save()
            return redirect('/game_app/games_list')
    else:
        edit_game_form = EditGame()
        return render(request, 'game_app/edit_game.html', {
            'edit_game_form': edit_game_form
        })


def registration(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            User.objects.create_user(username=registration_form.cleaned_data['username'],
                                     first_name=registration_form.cleaned_data['first_name'],
                                     last_name=registration_form.cleaned_data['last_name'],
                                     email=registration_form.cleaned_data['email'],
                                     password=registration_form.cleaned_data['password1'])
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


@login_required(login_url='/game_app/login')
@is_owner
def play(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if game.user.pk == request.user.pk:
        info = game.game_logs
        info_message = info["info_message"]
        hero = game.hero.get()
        monster = game.monster.get()
        monster_dialogs = ['На тобi КУРВА!', 'Отримуй!', 'Джета топ!', 'Получай!']

        def fight(hero_damage, attack_name):
            monster_damage = monster.level * 10
            info_message.append(f'{request.user}: hit by {attack_name} ({hero_damage} DMG)')
            monster.health = monster.health - hero_damage
            if monster.health <= 0 and monster.type == 'boss':
                info_message.append('You Won!!!')
                game.in_progress = False
            elif monster.health <= 0:
                if monster.level >= 5:
                    monster.level = 10
                    monster.health = 200
                    monster.max_health = 200
                    monster.type = 'boss'
                    monster.name = 'IGIBO'
                else:
                    hero.level = hero.level + 1
                    hero.health = 100 * hero.level
                    hero.max_health = 100 * hero.level
                    monster.level = monster.level + 1
                    monster.health = 50 * monster.level
                    monster.max_health = 50 * monster.level
            else:
                info_message.append(f'{monster.name}: O KURWA!')
                if hero.health <= monster_damage:
                    info_message.append('You Die!!!')
                    game.in_progress = False
                else:
                    if monster.type == 'monster':
                        info_message.append(f'{monster.name}: hit ({monster_damage} DMG)')
                        info_message.append(f'{monster.name}: {monster_dialogs[int(randint(0, 3))]}')
                    else:
                        boss_dialogs = ['Не больно', 'Слабак', 'Я неможу слухать цей бред']
                        info_message.append(f'{monster.name}: {boss_dialogs[int(randint(0, 3))]}')
                    hero.health = hero.health - monster_damage

        if hero.weapon.damage and (request.GET.get('attack') == 'hit'):
            weapon_damage = hero.weapon.damage
            weapon_name = hero.weapon.name
            fight(hero_damage=weapon_damage, attack_name=weapon_name)
        else:
            skill_damage = hero.skills.damage * hero.level * 0.8 * 10
            skill_name = hero.skills.name
            fight(hero_damage=skill_damage, attack_name=skill_name)

        game.game_logs = info
        game.save()
        hero.save()
        monster.save()

        return render(request, 'game_app/play.html', {
            'game': game,
            'hero': hero,
            'monster': monster,
            'hero_name': request.user,
            'info_message': info_message
        })
    else:
        return redirect(f'/game_app')
