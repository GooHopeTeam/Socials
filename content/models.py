from django.db import models

from society.models import Profile

from.validators import validate_file_extension


def upload_path(instance, name):
    return f'user_{instance.author.login}/{name}'


class BaseLike:
    objects, post, user = None, None, None

    def like(self, user, post):
        if self.objects.filter(user=user, post=post).exists():
            self.objects.get(user=user, post=post).delete()
        else:
            self.objects.create(user=user, post=post).save()

    def __str__(self):
        return f'{self.user.login} - {self.post}'


class Illustration(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    file = models.ImageField(upload_to=upload_path, validators=[validate_file_extension])


class IllustrationLike(BaseLike, models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, default=None)
    post = models.ForeignKey(Illustration, on_delete=models.CASCADE, related_name='likes')


class Video(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    file = models.FileField(upload_to=upload_path)


class VideoLike(BaseLike, models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, default=None)
    post = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')


class News(models.Model):
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    content = models.TextField()
    file = models.ImageField(upload_to=upload_path, blank=True, null=True, default=None)


class NewsLike(BaseLike, models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, default=None)
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='likes')


class Review(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    game_title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to=upload_path, blank=True, null=True, default=None)


class ReviewLike(BaseLike, models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, default=None)
    post = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
