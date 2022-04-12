from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from socials.utils import IRepositoryExtender
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

    def list(self, request, *args, **kwargs):
        illustrations = self.repository.list().values()
        for elem in illustrations:
            elem['likes'] = len(self.repository.get_likers(self.repository.get(elem.get('id'))))

        return Response(illustrations, status=status.HTTP_200_OK)
