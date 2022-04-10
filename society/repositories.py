from typing import Any, List, Union

from socials.utils import IRepository
from .models import Profile


class ProfileRepository(IRepository):
    model = Profile

    def get(self, pk: int) -> Union[Profile, None]:
        try:
            return self.model.objects.get(id=pk)
        except self.model.DoesNotExist:
            return None

    def list(self) -> List:
        return self.model.objects.all()

    def save(self, profile: Profile) -> None:
        profile.save()

    def delete(self, profile: Profile = None, pk: int = None):
        if profile:
            profile.delete()
        elif pk:
            profile = self.get(pk)
            self.delete(profile)
        else:
            raise AttributeError("Need 1 of 2 arguments")

    def create(self, **kwargs):
        raise NotImplementedError
