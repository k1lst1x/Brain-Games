from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('add_score/', views.add_score, name='add_score'),
	path('2048/', views.game_2048, name='game_2048'),
	path('marsmoney/', views.marsmoney, name='marsmoney'),
	path('mastercards/', views.mastercards, name='mastercards'),
	path('masterpieces/', views.masterpieces, name='masterpieces'),
	path('genius_memory/', views.genius_memory, name='genius_memory'),
	path('number_hunt/', views.number_hunt, name='number_hunt'),
	path('color_pairs/', views.color_pairs, name='color_pairs'),
	path('chess/', views.chess, name='chess'),
	path('match_the_feel/', views.match_the_feel, name='match_the_feel'),
	path('still_awake/', views.still_awake, name='still_awake'),
	path('leaderboard/', views.leaderboard_view, name='leaderboard'),
	path('profile/', views.profile_view, name='profile'),
]
