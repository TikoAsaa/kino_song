from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('song/', views.songs, name='song'),
    path('movies/', views.movies, name='movie'),
    path('song/song_info/<int:id>', views.song_info, name='song_info'),
    path('movies/movie_info/<int:id>', views.movie_info, name='movie_info'),
]
