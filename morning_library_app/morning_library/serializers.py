from rest_framework.serializers import ModelSerializer
from morning_library_app.morning_library.models import Track

class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"
