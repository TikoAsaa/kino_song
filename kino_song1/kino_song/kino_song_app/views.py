from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
from .models import Songs, Movies


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))


def songs(request):
    song = Songs.objects.all().values()
    template = loader.get_template('songs.html')
    context = {
        'my_songs': song,
    }
    return HttpResponse(template.render(context, request))


def movies(request):
    movie = Movies.objects.all().values()
    template = loader.get_template('movies.html')
    context = {
        'my_movies': movie,
    }
    return HttpResponse(template.render(context, request))


def song_info(request, id):
    song = Songs.objects.get(id=id)
    template = loader.get_template('song_info.html')
    context = {
        'my_song': song,
    }
    s = Songs.objects.get(id=id)
    s.song_views += 1
    s.save()
    return HttpResponse(template.render(context, request))


def movie_info(request, id):
    movie = Movies.objects.get(id=id)
    template = loader.get_template('movie_info.html')
    context = {
        'my_movie': movie,
    }
    m = Movies.objects.get(id=id)
    m.movie_views += 1
    m.save()
    return HttpResponse(template.render(context, request))


def add_view(request):
    v = Songs.song_views.objects.get(id=1)

    v.count += 1
    v.save()
    return render(request, 'song_info/{{ s.id }}')
