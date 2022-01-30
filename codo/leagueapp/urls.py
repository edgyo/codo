from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('start/', views.start, name='leaugeapp-start'),
    path('home/', views.home, name='leagueapp-home'),
    path('leaderboard/', views.leaderboard, name='leagueapp-leaderboard'),
    path('', RedirectView.as_view(url='start')),
]