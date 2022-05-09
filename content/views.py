from abc import ABC

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from socials.utils import IRepositoryExtender
from society.repositories import ProfileRepository
from .models import Illustration, News, Video, Review
from .repositories import IllustrationRepository, ReviewRepository, VideoRepository, NewsRepository
from .serializers import ReviewSerializer, IllustrationSerializer, VideoSerializer, NewsSerializer


class PostMixin(IRepositoryExtender,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                GenericViewSet, ABC):
    def list(self, request, *args, **kwargs):
        return Response(self.repository.get_all_posts(), status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response(self.repository.get_post(kwargs['pk']), status=status.HTTP_200_OK)


class IllustrationViewSet(PostMixin):
    queryset = Illustration.objects.all()
    serializer_class = IllustrationSerializer
    repository = IllustrationRepository()


class VideoViewSet(PostMixin):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    repository = VideoRepository()


class ReviewViewSet(PostMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    repository = ReviewRepository()


class NewsViewSet(PostMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    repository = NewsRepository()
