from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=25, blank=False, unique=True)
    duration = models.FloatField()
    numPlays = models.IntegerField()

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=25, blank=False, unique=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Genre(models.Model):
    type = models.CharField(max_length=25, blank=False, unique=True)

    def __str__(self):
        return self.type

