from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Game, Included, Category


# Navbar Category selection
def all_games(request):
    games = Game.objects.all()
    included = Included.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            games = games.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    # User Search
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter one or more words to search for")
                return redirect(reverse('games'))

            # Apply the search query to the Included model (item field)
            i_queries = Q(item__icontains=query)
            items = included.filter(i_queries)
            for i in items:
                print(i.game)

            # Apply the search query to the Games model (name and description fields, plus the items of the preovius search)
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
