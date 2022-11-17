from django.db import models

# Create your models here.
class song(models.Model):
    title = models.CharField(max_length=25, blank=False, unique=True)
    duration = models.FloatField()
    numPlays = models.IntegerField()

    def __str__(self):
        return self.title