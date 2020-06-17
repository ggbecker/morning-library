from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchQuery, SearchVector

import django_filters

from .utils import length_to_formatted_length

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
        return length_to_formatted_length(self.length)


    def bitrate_in_kilobits(self):
        return "{}kbps".format(int(int(self.bitrate)/1000))


class TrackFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='multiple_field_search', label='Search')

    class Meta:
        model = Track
        # fields = ['title', 'artist', 'album', 'path']
        fields = ['search']

    def multiple_field_search(self, queryset, name, value):
        return Track.objects.annotate(search=SearchVector('title','artist', 'album', 'path')).filter(search=SearchQuery(value))
