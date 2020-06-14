from django.db import models
from django.contrib.auth.models import User

import django_filters
import datetime

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

    def get_length_formatted(self):
        length_formatted = str(datetime.timedelta(seconds=float(self.length)))
        if length_formatted[0] == "0" and length_formatted[1] == ":":
            length_formatted = length_formatted[2:]
        return length_formatted.split(".")[0]


class TrackFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    artist = django_filters.CharFilter(lookup_expr='icontains')
    album = django_filters.CharFilter(lookup_expr='icontains')
    path = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Track
        fields = ['title', 'artist', 'album', 'path']
