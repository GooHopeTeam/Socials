from abc import ABC, abstractmethod
from typing import List, Any


class IRepository(ABC):
    """ Repository's Interface """

    @property
    @abstractmethod
    def model(self):
        """ Repository model """

    def get(self, pk: int) -> Any:
        """ Return object by id """
        try:
            return self.model.objects.get(id=pk)
        except self.model.DoesNotExist:
            return None

    def list(self) -> List:
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

    def create(self, **kwargs) -> None:
        """ Create object with params """
        self.save(self.model.objects.create(kwargs))


class IRepositoryExtender(ABC):
    """ Repository class contain """

    @property
    @abstractmethod
    def repository(self):
        """ Repository """
