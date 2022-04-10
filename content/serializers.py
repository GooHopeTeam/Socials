from rest_framework import serializers

from .models import Illustrations, News, Reviews, Videos


class IllustrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustrations
        fields = '__all__'


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
