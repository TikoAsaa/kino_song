from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('song/', views.songs, name='song'),
    path('movies/', views.movies, name='movie'),
    path('song/update/<int:id>', views.update, name='update'),
]
