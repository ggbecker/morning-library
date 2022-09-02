import django_tables2 as tables
from .models import Track
from django.utils.translation import gettext_lazy as _

class TrackTable(tables.Table):
    length = tables.Column(accessor='get_length_formatted', verbose_name=_('Length'), orderable=False)
    bitrate = tables.Column(accessor='bitrate_in_kilobits', verbose_name=_('Bitrate'), orderable=False)

    class Meta:
        model = Track
        template_name = "django_tables2/bootstrap4.html"
        fields = ("title", "artist", "album", "year", "length", "codec", "bitrate", "location", "path")
        # attrs = {"class": "table"}
