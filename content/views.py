from rest_framework.viewsets import mixins, GenericViewSet

from .models import Illustration, New, Video, Review
from .serializers import ReviewSerializer, IllustrationSerializer, VideoSerializer, NewsSerializer


class IllustrationViewSet(mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = Illustration.objects.all()
    serializer_class = IllustrationSerializer
