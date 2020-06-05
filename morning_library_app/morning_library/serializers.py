from rest_framework import serializers
from .models import Track

class TrackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        item = Track.objects.create(user=self.context['request'].user, **validated_data)
        return item
    class Meta:
        model = Track
        fields = "__all__"
