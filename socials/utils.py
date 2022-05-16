from abc import ABC, abstractmethod
from typing import Any

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import status


class IRepository(ABC):
    """ Repository's Interface """

    @property
    @abstractmethod
    def model(self):
        """ Repository model """

    def get(self, pk: int) -> Any:
        """ Return object by id """
        return get_object_or_404(self.model, id=pk)

    def list(self) -> QuerySet:
        """ Return all objects from model """
        return self.model.objects.all()

    def save(self, obj: Any) -> None:
        """ Save updated object """
        obj.save()

    def delete(self, obj: Any = None, pk: int = None) -> None:
        """ Delete object (by id) """
        if obj:
            obj.delete()
        elif pk:
            obj = self.get(pk)
            if obj:
                self.delete(obj)
        else:
            raise AttributeError

    def create(self, **kwargs) -> int:
        """ Create object with params """
        self.save(self.model.objects.create(**kwargs))

        return status.HTTP_201_CREATED


class IRepositoryExtender(ABC):
    """ Repository class contain """

    @property
    @abstractmethod
    def repository(self):
        """ Repository """
