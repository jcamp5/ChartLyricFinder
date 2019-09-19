from django.db import models

# Create your models here.


class Song(models.Model):
    rank = models.IntegerField()
    title = models.CharField(max_length=75)
    artist = models.CharField(max_length=75)
    lyrics = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.rank} | {self.title} | {self.artist}"