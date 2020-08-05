from django.shortcuts import render
from .models import Game


# Show all the games on sale on the site
def all_games(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'games/games.html', context)