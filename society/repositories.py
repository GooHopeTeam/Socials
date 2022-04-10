from typing import List, Union

from socials.utils import IRepository
from .models import Profile


class ProfileRepository(IRepository):
    model = Profile
