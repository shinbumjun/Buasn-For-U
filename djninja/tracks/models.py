from django.db import models

# Create your models here.
from django.db import models

class Track(models.Model): # tracks.json이랑 연관
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250) 
    duration = models.FloatField()
    last_play = models.DateTimeField()