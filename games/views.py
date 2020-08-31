from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Game, Included, Category
from .forms import GameForm, IncludedForm


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
                messages.info(request, "Please enter one or more words to search for")
                return redirect(reverse('games'))
            
            # Search in the name and description fields of the Game model
            g_queries = Q(name__icontains=query) | Q(description__icontains=query)

            # Search in the item field of the Included model
            i_queries = Q(item__icontains=query)
            included = included.filter(i_queries) 
            
            # Extend the search in the game model with the results of the search in the Included model
            for i in included:
                g_queries = g_queries | Q(name__icontains=i.game.name)

            games = games.filter(g_queries)

    context = {
        'games': games,
        'search_term': query,
        'categories': categories,
    }

    return render(request, 'games/games.html', context)


# Show the details of a specific game
def game_details(request, game_pk):

    game = get_object_or_404(Game, pk=game_pk)

    # All the other games in the same category
    games = Game.objects.filter(category=game.category).exclude(pk = game_pk)
    
    # The instance of Included whose foreign key is the same as the selected Game instance
    included = Included.objects.filter(game=game_pk)

    context = {
        'game': game,
        'included': included,
        'games': games
    }

    return render(request, 'games/game_details.html', context)
