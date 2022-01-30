from django.http import HttpResponse
from django.shortcuts import render

leaderboard_dict = [
    {
        'nickname': 'edgepy',
        'codo_rating': '4592',
        'csgo_elo': '2592',
        'dota2_elo': '2000'
    },
    {
        'nickname': 'rekted',
        'codo_rating': '5000',
        'csgo_elo': '3000',
        'dota2_elo': '2000'
    },
]

def start(request):
    return render(request, 'leagueapp/start.html')

def home(request):
    return render(request, 'leagueapp/home.html')

def leaderboard(request):
    context = {
        'leaderboard': leaderboard_dict
    }
    return render(request, 'leagueapp/leaderboard.html', context)