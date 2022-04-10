from rest_framework import serializers

from .models import Illustration, New, Review, Video


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
        model = New
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
