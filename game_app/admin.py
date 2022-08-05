from django.contrib import admin

from .models import Game, Monster, Hero, Weapon

admin.site.register(Game)
admin.site.register(Monster)
admin.site.register(Hero)
admin.site.register(Weapon)
