from rest_framework.serializers import ModelSerializer
from morning_library_app.morning_library.models import LibraryEntry, Track


class LibraryEntrySerializer(ModelSerializer):
    class Meta:
        model = LibraryEntry
        fields = "__all__"


class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"
