from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_games, name='games'),
    path('<game_pk>', views.game_details, name='game_details'),
]