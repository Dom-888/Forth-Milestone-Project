from django.shortcuts import render, get_object_or_404
from .models import Game, Included


# Show all the games on sale on the site
def all_games(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'games/games.html', context)


# Show the details of a specific game
def game_details(request, game_pk):

    game = get_object_or_404(Game, pk=game_pk)

    # I need a way to select only the icluded instance where included.game = game.pk
    included = Included.objects.all()

    context = {
        'game': game,
        'included': included
    }

    return render(request, 'games/game_details.html', context)