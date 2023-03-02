from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:team_id>/', views.detail, name='detail'),
    path('match/', views.match, name='match'),
    path('playMatch/',views.playMatch, name='playMatch'),
    path('<int:team_id>/players/<int:player_id>/', views.detail_player, name='detail_player'),
]