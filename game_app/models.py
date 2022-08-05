from django.db import models


class Game(models.Model):
    game_name = models.CharField(max_length=200, unique=True)
    in_progress = models.BooleanField(default=True)
    game_logs = models.JSONField("ContactInfo", default=dict)


class Monster(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='monster')
    name = models.CharField(max_length=200, unique=True)
    health = models.IntegerField(default=60)
    level = models.IntegerField(default=1)


class Weapon(models.Model):
    name = models.CharField(max_length=200, unique=True)
    damage = models.IntegerField(unique=True)


class Hero(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='hero')
    health = models.IntegerField(default=100)
    level = models.IntegerField(default=1)
    weapon = models.ManyToManyField(Weapon)

    def __str__(self):
        return f'Hero - {self.health}'
