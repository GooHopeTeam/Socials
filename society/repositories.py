from typing import List, Union

from socials.utils import IRepository
from .models import Profile, Society, SocietyMembers, SocietyComments


class ProfileRepository(IRepository):
    model = Profile


class SocietyRepository(IRepository):
    model = Society


class SocietyMembersRepository(IRepository):
    model = SocietyMembers


class SocietyCommentsRepository(IRepository):
    model = SocietyComments
