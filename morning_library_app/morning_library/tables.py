import django_tables2 as tables
from .models import Track

class TrackTable(tables.Table):
    length = tables.Column(accessor='get_length_formatted', verbose_name='Length', orderable=False)

    class Meta:
        model = Track
        template_name = "django_tables2/bootstrap.html"
        fields = ("title", "artist", "album", "year", "length", "codec", "location", "rating", "path")
        # attrs = {"class": "table"}
