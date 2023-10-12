from rest_framework import serializers
from .models import YouTubeVideo

class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = ["title", "channel"]