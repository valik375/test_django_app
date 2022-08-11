from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    game_name = models.CharField(max_length=200, unique=True)
    in_progress = models.BooleanField(default=True)
    game_logs = models.JSONField("ContactInfo", default=dict)

    def __str__(self):
        return f'{self.pk}) {self.game_name}'


class Monster(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='monster')
    name = models.CharField(max_length=200)
    max_health = models.IntegerField(default=60)
    health = models.IntegerField(default=60)
    level = models.IntegerField(default=1)
    type = models.CharField(default='monster', max_length=200)
    money = models.IntegerField(default=10)


class Weapon(models.Model):
    name = models.CharField(max_length=200, unique=True)
    damage = models.IntegerField(unique=True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Skills(models.Model):
    name = models.CharField(max_length=200, unique=True)
    damage = models.IntegerField(default=20)

    def __str__(self):
        return f'{self.name} - DMG:{self.damage}'


class Hero(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='hero')
    max_health = models.IntegerField(default=100)
    health = models.IntegerField(default=100)
    level = models.IntegerField(default=1)
    weapon = models.ForeignKey(Weapon, on_delete=models.SET_NULL, null=True)
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True)
    money = models.IntegerField()

    def __str__(self):
        return f'Hero - {self.health}'


class Shop(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='shop')
    weapon = models.ManyToManyField(Weapon)

