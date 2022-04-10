from rest_framework.viewsets import GenericViewSet, mixins

from .models import Dialog
from .serializers import DialogSerializer


class DialogsViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Dialog.objects.all()
    serializer_class = DialogSerializer
