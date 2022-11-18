from django.db import models

class Genre(models.Model):
    type = models.CharField(max_length=25, blank=False, unique=True)

    def __str__(self):
        return self.type


class Song(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True)
    duration = models.FloatField()
    numPlays = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=25, blank=False, unique=True)
    release_date = models.DateField()
    # By using "related_name", we can now say song.albums AND album.songs
    # In other words, before we could only answer "given an album, what songs does it have?"
    # Now we can answer "given a song, what albums contain it?"
    songs = models.ManyToManyField(Song, related_name='albums')

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=25, blank=False, unique=True)
    created = models.DateTimeField()
    Total_songs = models.IntegerField()
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=200, blank= False, unique=True)
    age = models.IntegerField()
    song = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)