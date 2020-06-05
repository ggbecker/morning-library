from django.db import models
from django.contrib.auth.models import User

class Rating(models.IntegerChoices):
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

class Track(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(max_length=255, blank=True, null=True)
    album = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    length = models.CharField(max_length=255, blank=True, null=True)
    codec = models.CharField(max_length=255, blank=True, null=True)
    sample_rate = models.CharField(max_length=255, blank=True, null=True)
    bitrate = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(null=True, choices=Rating.choices)
    timestamp = models.DateTimeField(auto_now=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
