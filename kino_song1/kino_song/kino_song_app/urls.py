from django.urls import path

from . import views

app_name = 'song'
urlpatterns = [
    path('', views.home, name='home'),
    path('song/', views.songs, name='song'),
    path('movies/', views.movies, name='movie'),
]
