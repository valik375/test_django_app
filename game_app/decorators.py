from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render

from .models import Game


def is_owner(function):
    def wrapper(request, game_id):
        game = get_object_or_404(Game, pk=game_id)
        if int(request.user.pk) == int(game.user.pk):
            return function(request, game_id)
        else:
            return redirect('/game_app/')
    return wrapper
