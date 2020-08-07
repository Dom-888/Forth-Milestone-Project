from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Game, Included


# Show the games on sale on the site
def all_games(request):
    games = Game.objects.all()
    included = Included.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter one or more words to search for")
                return redirect(reverse('games'))

            # Apply the search query to the Included model
            i_queries = Q(item__icontains=query)
            items = included.filter(i_queries)
            for i in items:
                print(i.game)


            # Apply the search query to the Games 
            g_queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(name__icontains=i.game) 
            games = games.filter(g_queries)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'games/games.html', context)


# Show the details of a specific game
def game_details(request, game_pk):

    game = get_object_or_404(Game, pk=game_pk)

    # Select the instance of included whose foreign key is the same as the selected game instance
    included = Included.objects.filter(game=game_pk)

    context = {
        'game': game,
        'included': included,
    }

    return render(request, 'games/game_details.html', context)
