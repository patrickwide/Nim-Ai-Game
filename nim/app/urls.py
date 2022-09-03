from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
    path('game', views.game, name='game'),
    path('api', views.api, name='api'),
]
