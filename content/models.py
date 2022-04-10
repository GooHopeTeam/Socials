from django.db import models

from society.models import Profile

LIKE_STATUS = (
    ('Liked', 'Liked'),
    ('Report', 'Report'),
    ('None', 'None'),
)


def upload_path(instance, name):
    return f'user_{instance.author.login}/{name}'


class Illustrations(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    likes = models.PositiveIntegerField(blank=True, default=0)
    liked = models.CharField(max_length=8, choices=LIKE_STATUS)
    image = models.ImageField(upload_to=upload_path)


class Videos(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    likes = models.PositiveIntegerField(blank=True, default=0)
    liked = models.CharField(max_length=8, choices=LIKE_STATUS)
    video = models.FileField(upload_to=upload_path)


class News(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    content = models.TextField()
    likes = models.PositiveIntegerField(blank=True, default=0)
    liked = models.CharField(max_length=8, choices=LIKE_STATUS)
    image = models.ImageField(upload_to=upload_path, blank=True, null=True, default=None)


class Reviews(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(blank=True, default=0)
    liked = models.CharField(max_length=8, choices=LIKE_STATUS)
    image = models.ImageField(upload_to=upload_path, blank=True, null=True, default=None)
