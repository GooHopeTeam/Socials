from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from socials.utils import IRepositoryExtender
from society.repositories import ProfileRepository
from .models import Illustration, New, Video, Review
from .repositories import IllustrationRepository, ReviewRepository, VideoRepository, NewRepository
from .serializers import ReviewSerializer, IllustrationSerializer, VideoSerializer, NewsSerializer


class IllustrationViewSet(IRepositoryExtender,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = Illustration.objects.all()
    serializer_class = IllustrationSerializer
    repository = IllustrationRepository()

    def retrieve(self, request, *args, **kwargs):
        return Response({
            self.repository.is_liked(self.repository.get(kwargs.get('pk')), ProfileRepository().get(3))
        }, status=status.HTTP_200_OK)
