from abc import ABC, abstractmethod
from profile import Profile
from typing import List, Union, Any

from socials.utils import IRepository
from .models import New, Video, Illustration, Review


class IContentRepository(IRepository, ABC):
    def get_by_author(self, author: Profile) -> List[Any]:
        return self.model.objects.filter(author=author)

    def get_by_game(self, game_title: str) -> List[Any]:
        return self.model.objects.filter(game_title=game_title)

    @abstractmethod
    def get_likers(self, post: Any) -> List[Profile]:
        pass

    @abstractmethod
    def is_liked(self, profile: Profile) -> bool:
        pass


class NewsRepository(IContentRepository):
    model = New

    def get_likers(self, post: New) -> List[Profile]:
        likers = post.liked

    def is_liked(self, profile: Profile) -> bool:
        pass

    def get(self, pk: int) -> Union[New, None]:
        try:
            return self.model.objects.get(id=pk)
        except self.model.DoesNotExist:
            return None

    def list(self) -> List:
        return self.model.objects.all()

    def save(self, news: New) -> None:
        news.save()

    def delete(self, news: New = None, pk: int = None):
        if news:
            news.delete()
        elif pk:
            news = self.get(pk)
            if news:
                self.delete(news)
        else:
            raise AttributeError

    def create(self, **kwargs):
        raise NotImplementedError
