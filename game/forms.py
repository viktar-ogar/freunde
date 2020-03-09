from django import forms

class GameForm(forms.Form):
    number_players = forms.IntegerField(min_value=2, label="Количество игроков")
    win_score = forms.IntegerField(min_value=0, label="Количество очков для победы")

class PlayersForm(forms.Form):
    name = forms.CharField(min_length=1, label="Имя игрока", widget=forms.TextInput(attrs={'placeholder': 'Имя игрока'}))
    scores = forms.IntegerField(min_value=0, label="Количество очков")

class RoundForm(forms.Form):
    score = forms.IntegerField(min_value=0, label="Количество очков")
    