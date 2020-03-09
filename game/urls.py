from django.urls import path
from . import views as game_views

urlpatterns = [
    path('', game_views.index),
    path('create_players/', game_views.create_players),
    path('edit/<int:id>', game_views.edit),
    path('delete/<int:id>', game_views.delete),
    path('process/', game_views.process),
    path('endgame/', game_views.endgame),
]