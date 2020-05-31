from django.db import models

# Create your models here.

from django.db import models

class Rating(models.IntegerChoices):
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    length = models.CharField(max_length=255)


class LibraryEntry(models.Model):
    path = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    owner = models.CharField(max_length=255, unique=True)
    rating = models.IntegerField(null=True, blank=True, choices=Rating.choices)
    timestamp = models.DateTimeField(auto_now=True)
