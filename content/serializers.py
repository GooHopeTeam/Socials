from rest_framework import serializers

from .models import Illustration, News, Review, Video


class IllustrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustration
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
