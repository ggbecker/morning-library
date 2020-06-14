from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django_tables2 import SingleTableView
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import Track, TrackFilter
from .tables import TrackTable
from .serializers import TrackSerializer

class TrackViewSet(generics.CreateAPIView):
    serializer_class = TrackSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TrackListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Track
    table_class = TrackTable
    login_url = '/login/'
    template_name = 'morning_library/track_list.html'
    filterset_class = TrackFilter
    # redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Track.objects.filter(user=self.request.user)


class APITokenView(LoginRequiredMixin, ListView):
    model = Token
    login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    def get_queryset(self):
        token = Token.objects.get_or_create(user=self.request.user)
        return Token.objects.filter(user=self.request.user)
