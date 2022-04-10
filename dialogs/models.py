from django.db import models

from society.models import Profile


class Dialog(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='User')
    friend = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='Friend')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.login} - {self.friend.login}'


class Messages(models.Model):
    dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
    message = models.CharField(max_length=800)
    sender = models.ForeignKey(Profile, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.sender} - {self.message[:15]}'

