from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from rest_framework import viewsets

from morning_library_app.morning_library.models import Track
from morning_library_app.morning_library.serializers import TrackSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackListView(ListView):
    model = Track
