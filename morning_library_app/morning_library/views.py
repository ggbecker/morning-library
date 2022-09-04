from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.urls import reverse
from django.contrib.auth import login

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

from .utils import length_to_formatted_length

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


@login_required(login_url='/login/')
def statistics(request):
    codec_statistics = {}
    track_distinct_list = Track.objects.filter(user=request.user).values('codec').distinct()
    for track in track_distinct_list:
        codec = track.get('codec')
        if codec:
            codec_statistics.update({codec: Track.objects.filter(user=request.user, codec=codec).count()})

    track_count = Track.objects.filter(user=request.user).count()
    total_length = length_to_formatted_length(Track.objects.filter(user=request.user).annotate(length_as_float=Cast('length', FloatField())).aggregate(Sum('length_as_float'))['length_as_float__sum'])

    return render(request, 'morning_library/statistics.html', {'statistics':
        {
            'codec_statistics': codec_statistics,
            'track_count': track_count,
            'total_length': total_length,
        }
    })


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
    context['form']=form
    return render(request,'registration/sign_up.html',context)


def about(request):
    return render(request, 'morning_library/about.html')


def index(request):
    return render(request, 'morning_library/index.html')


class APITokenView(LoginRequiredMixin, ListView):
    model = Token
    login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    def get_queryset(self):
        token = Token.objects.get_or_create(user=self.request.user)
        return Token.objects.filter(user=self.request.user)
