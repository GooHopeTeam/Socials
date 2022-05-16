from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from socials.utils import IRepositoryExtender
from . import detail_messages as errors
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
        self.repository.create(user=request.POST.get('friend'), friend=request.POST.get('user'))  # Create dialog to the friend
        return super(DialogsViewSet, self).create(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        dialog = self.repository.get(kwargs.get('pk'))
        if not dialog:
            return Response({
                'detail': errors.DIALOG_NO_ACCESS
            }, status=status.HTTP_403_FORBIDDEN)
        return super(DialogsViewSet, self).retrieve(request, args, kwargs)

    def list(self, request, *args, **kwargs):
        return Response(self.repository.list().values(), status=status.HTTP_200_OK)


class MessageViewSet(IRepositoryExtender,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    repository = MessagesRepository()

    def list(self, request, *args, **kwargs):
        dialog = DialogRepository().get(kwargs['dialog_id'])
        if not dialog:
            return Response({
                'detail': errors.DIALOG_NO_ACCESS
            }, status=status.HTTP_403_FORBIDDEN)

        return Response(self.repository.list().filter(dialog=dialog).values(), status=status.HTTP_200_OK)
