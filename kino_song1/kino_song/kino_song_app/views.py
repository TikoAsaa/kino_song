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
    return HttpResponse(template.render(context, request))
