from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from socials import settings
from socials.utils import IRepositoryExtender
from .models import Message, Dialog
from .repositories import MessagesRepository, DialogRepository
from .serializers import MessageSerializer, DialogSerializer


class DialogsViewSet(IRepositoryExtender,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Dialog.objects.all()
    serializer_class = DialogSerializer
    repository = DialogRepository()

    def create(self, request, *args, **kwargs):
        # Create dialog to the friend
        self.repository.create(user=request.POST.get('friend'), friend=request.POST.get('user'))
        return super(DialogsViewSet, self).create(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        return self.repository.get(kwargs.get('pk')) or super(DialogsViewSet, self).retrieve(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        return Response(self.repository.list().values(), status=status.HTTP_200_OK)


class MessageViewSet(IRepositoryExtender,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    repository = MessagesRepository()
