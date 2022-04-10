from abc import ABC
from profile import Profile
from typing import List, Any

from content.models import Illustration, New, Review, Video
from socials.utils import IRepository


class IContentRepository(IRepository, ABC):
    def get_by_author(self, author: Profile) -> List[Any]:
        return self.model.objects.filter(author=author)

    def get_by_game(self, game_title: str) -> List[Any]:
        return self.model.objects.filter(game_title=game_title)

    def get_likers(self, post: Any) -> List[Profile]:
        if post in self.list():
            return post.likes.all()

    def is_liked(self, post: Any, profile: Profile) -> bool:
        if post in self.list():
            return post.likes.filter(user=profile).exists()


class IllustrationRepository(IContentRepository):
    model = Illustration


class NewRepository(IContentRepository):
    model = New


class VideoRepository(IContentRepository):
    model = Video


class ReviewRepository(IContentRepository):
    model = Review
