from django.db import models


class Game(models.Model):
    user_name = models.CharField(max_length=200, unique=True)
    user_id = models.AutoField(primary_key=True)
    in_progress = models.BooleanField(True)
