from django.db import models


class Game(models.Model):
    # change to game_name
    user_name = models.CharField(max_length=200, unique=True)
    # change to game_id
    user_id = models.AutoField(primary_key=True)
    in_progress = models.BooleanField(True)
    # create game_logs (info_message)
