from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=25)
    duration = models.DateField()
    numPlays = models.IntegerField()

    def __str__(self):
        return self.title

