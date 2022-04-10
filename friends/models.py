from django.db import models

from society.models import Profile


class Friends(models.Model):
    status_choices = (
        ('FAV', 'Favorite'),
        ('NEU', 'Neutral'),
        ('BL', 'Blocked')
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    friend = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend')
    status = models.CharField(choices=status_choices, max_length=15)

    def __str__(self):
        return f'user: {self.user} / friend: {self.friend}'

    @classmethod
    def contains_friend(cls, friend, user=None):
        return cls.objects.filter(user=user or cls.user, friend=friend)

    @classmethod
    def get_friends(cls, user=None):
        return cls.objects.filter(user=user or cls.user)
