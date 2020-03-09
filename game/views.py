from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Players, Game, Round
from .forms import GameForm, PlayersForm, RoundForm


# получение данных из бд
def index(request):
    players = Players.objects.all()
    game_form = PlayersForm()
    return render(request, "game/index.html", context={'players': players, 'game_form': game_form})


# # сохранение данных в бд
# def create_game(request):
#     players = Players.objects.all()
#     if request.method == "POST":
#         game = Game()
#         game.number_players = request.POST.get("number_players")
#         game.win_score = request.POST.get("win_score")
#         game.save()
#         game_form = PlayersForm()
#     return render(request, "game/game-start.html", context={'game': game, 'game_form': game_form, 'players': players})


# сохранение данных в бд
def create_players(request):
    players = Players.objects.all()
    game_form = PlayersForm()
    if request.method == "POST":
        player = Players()
        player.name = request.POST.get("name")
        player.save()
    return render(request, "game/index.html", context={'game_form': game_form, 'players': players})


# изменение данных в бд
def edit(request, id):
    try:
        player = Players.objects.get(id=id)
 
        if request.method == "POST":
            player.name = request.POST.get("name")
            player.scores = request.POST.get("scores")
            player.save()
            return HttpResponseRedirect("/game/create_players/")
        else:
            player_form = PlayersForm()
            return render(request, "game/edit.html", {'players': player, 'player_form': player_form})
    except Players.DoesNotExist:
        return HttpResponseNotFound("<h2>Player not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        player = Players.objects.get(id=id)
        player.delete()
        return HttpResponseRedirect("/game/create_players/")
    except Players.DoesNotExist:
        return HttpResponseNotFound("<h2>Player not found</h2>")


def process(request):
    round_form = RoundForm()
    players = Players.objects.all()
    if request.method == "POST":
        if request.POST.get("winner"):
            winner_id = request.POST.get("winner")
            scores_of_round = request.POST.get("score")
            player = Players.objects.get(id=winner_id)
            player.scores += int(scores_of_round)
            player.save()
    return render(request, "game/process.html", context={'round_form': round_form, 'players': players})


def endgame(request):
    players = Players.objects.all()
    for player in players:
        player.scores = 0
        player.save()
    return HttpResponseRedirect("/game/")
