from rest_framework.viewsets import mixins, GenericViewSet

from .models import Illustrations, News, Videos, Reviews
from .serializers import ReviewsSerializer, IllustrationSerializer, VideosSerializer, NewsSerializer


class IllustrationViewSet(mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    queryset = Illustrations.objects.all()
    serializer_class = IllustrationSerializer
