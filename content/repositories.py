from abc import ABC
from profile import Profile
from typing import List, Any, Dict

from django.db.models import QuerySet
from django.forms import model_to_dict
from rest_framework import status

from content.models import Illustration, News, Review, Video
from socials.utils import IRepository


class IContentRepository(IRepository, ABC):
    def get_by_author(self, author: Profile) -> QuerySet:
        return self.model.objects.filter(author=author)

    def get_by_game(self, game_title: str) -> QuerySet:
        return self.model.objects.filter(game_title=game_title)

    def get_likers(self, post: Any) -> QuerySet:
        if post in self.list():
            return post.likes.all()

    def is_liked(self, post: Any, profile: Profile) -> bool:
        if post in self.list():
            return post.likes.filter(user=profile).exists()

    def get_all_posts(self) -> List[Dict]:
        for elem in self.list():
            yield self.get_post(elem.id)

    def get_post(self, pk: int) -> Dict:
        post = model_to_dict(self.get(pk))
        post['likes'] = len(self.get_likers(self.get(pk)))
        post['file'] = post['file'].url

        return post


class IllustrationRepository(IContentRepository):
    model = Illustration


class NewsRepository(IContentRepository):
    model = News


class VideoRepository(IContentRepository):
    model = Video


class ReviewRepository(IContentRepository):
    model = Review
