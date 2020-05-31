from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from morning_library_app.morning_library.models import LibraryEntry, Track
from morning_library_app.morning_library.serializers import LibraryEntrySerializer, TrackSerializer


class LibraryEntryViewSet(viewsets.ModelViewSet):
    queryset = LibraryEntry.objects.all()
    serializer_class = LibraryEntrySerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
