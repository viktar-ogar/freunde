from django.db import models

class Players(models.Model):
    name = models.CharField(max_length=120)
    wins = models.SmallIntegerField(verbose_name="Победы игрока", default=0)
    scores = models.SmallIntegerField(verbose_name="Количество очков хода", default=0)
    winner = models.BooleanField(default=False)


class Game(models.Model):
    number_players = models.IntegerField(verbose_name="Количество игроков")
    win_score = models.SmallIntegerField(verbose_name="Количество очков для победы")


class Round(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    winner = models.ForeignKey(Players, on_delete=models.CASCADE)
    score = models.SmallIntegerField(verbose_name="Количество очков хода", default=0)
