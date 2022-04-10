from django.conf import settings
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from friends.models import Friends
from .models import Profile, Society
from .serializers import UserSerializer


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

    @staticmethod
    def visibility_regulator(user: Profile.objects, profile: Profile) -> bool:
        """
        :param user: Current user
        :param profile: Opened profile
        :return: Profile status (hidden or visible)
        """
        hidden = False
        if not profile.publicity == Profile.publicity_choices[0][0]:
            profile_friends = profile.friend.all()
            hidden = True
            if profile_friends:
                # Friend and friends of friends
                if profile.publicity == Profile.publicity_choices[1][0]:
                    if not Friends.contains_friend(profile, user):
                        if [x for x in [Friends.contains_friend(user, x.user) for x in profile_friends if x] if x]:
                            hidden = False
                    else:
                        hidden = False

                # Just friends
                elif profile.publicity == Profile.publicity_choices[2][0]:
                    if Friends.contains_friend(profile, user):
                        hidden = False
        return hidden

    def retrieve(self, request, *args, **kwargs):
        _id = kwargs.get('pk')

        user = Profile.objects.get(id=settings.USER_ID)
        profile = get_object_or_404(self.queryset, id=_id)
        _profile = model_to_dict(profile, ('avatar', 'login', 'status', 'description'))
        _profile['avatar'] = profile.avatar.name

        return Response({
            'user': _profile,
            'hidden': ProfileViewSet.visibility_regulator(user, profile),
            'friends': Profile.objects.filter(user_id__in=profile.friend.all().values('user_id')).values(),
            'societies': Society.objects.filter(societymembers__user=profile).values()
        }, status=status.HTTP_200_OK)
