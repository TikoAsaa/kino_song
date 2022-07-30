from django.db import models

# Create your models here.


class Songs(models.Model):
    objects = None
    song_name = models.CharField(max_length=255)
    song_artist = models.CharField(max_length=255)
    song_data = models.CharField(max_length=6)
    song_views = models.IntegerField(default=0)

    def __str__(self):
        return "{} {} - Data - {} Views - {}".format(self.song_name, self.song_artist, self.song_data, self.song_views)


class Movies(models.Model):
    objects = None
    movie_name = models.CharField(max_length=255)
    movie_artist = models.CharField(max_length=255)
    movie_data = models.CharField(max_length=6)
    movie_views = models.IntegerField(default=0)

    def __str__(self):
        return "{} {} - Data - {} Views - {}".format(self.movie_name, self.movie_artist, self.movie_data, self.movie_views)