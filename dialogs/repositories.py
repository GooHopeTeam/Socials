from typing import Any

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.response import Response

from socials import settings
from socials.utils import IRepository
from society.repositories import ProfileRepository
from .models import Dialog, Message


class DialogRepository(IRepository):
    model = Dialog

    def list(self) -> QuerySet:
        return super(DialogRepository, self).list().filter(user=ProfileRepository().get(settings.USER_ID))

    def create(self, **kwargs) -> int:
        return super(DialogRepository, self).create(user=ProfileRepository().get(kwargs.get('user')),
                                                    friend=ProfileRepository().get(kwargs.get('friend')))

    def get(self, pk: int) -> Any:
        if super(DialogRepository, self).get(pk) not in self.list():
            return Response({
                'detail': 'Unable to start conversation. No user found or you do not have access to this conversation.'
            }, status=status.HTTP_403_FORBIDDEN)
        return None


class MessagesRepository(IRepository):
    model = Message
