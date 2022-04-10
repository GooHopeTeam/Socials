from abc import ABC, abstractmethod
from typing import List, Any


class IRepository(ABC):
    """ Repository's Interface """

    @property
    @abstractmethod
    def model(self):
        """ Repository model """

    @abstractmethod
    def get(self, pk: int) -> Any:
        """ Return object by id """

    @abstractmethod
    def list(self) -> List:
        """ Return all objects from model """

    @abstractmethod
    def save(self, obj: Any) -> None:
        """ Save updated object """

    @abstractmethod
    def delete(self, obj: Any = None, pk: int = None) -> None:
        """ Delete object (by id) """

    @abstractmethod
    def create(self, **kwargs) -> None:
        """ Create object with params """


class IRepositoryExtender(ABC):
    """ Repository class contain """

    @property
    @abstractmethod
    def repository(self):
        """ Repository """
