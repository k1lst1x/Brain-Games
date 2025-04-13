from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('2048/', views.game_2048, name='game_2048'),
	path('marsmoney/', views.marsmoney, name='marsmoney'),
	path('mastercards/', views.mastercards, name='mastercards'),
	path('masterpieces/', views.masterpieces, name='masterpieces'),
	path('genius_memory/', views.genius_memory, name='genius_memory'),
]
