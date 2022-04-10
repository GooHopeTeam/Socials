from django.db import models


class Profile(models.Model):
    publicity_choices = (
        ('ALL', 'All'),
        ('FaF', 'Friend and friends of friends'),
        ('JF', 'Just friends'),
        ('OO', 'Only owner')
    )

    def upload_path(self, *args):
        return f'user_{self.login}/{args[0]}'

    user_id = models.IntegerField(unique=True)
    login = models.CharField(null=True, blank=True, max_length=30)
    avatar = models.ImageField(upload_to=upload_path, blank=True, null=True, default=None)
    status = models.BooleanField(default=True)
    publicity = models.CharField(choices=publicity_choices, max_length=50)
    description = models.CharField(max_length=220, null=True, blank=True)

    def __str__(self):
        return f'User: {self.user_id} {self.login} - {self.publicity}'


class Society(models.Model):
    title = models.CharField(max_length=55, unique=True)
    image = models.ImageField(upload_to=f'society_{title}/', blank=True, null=True, default=None)
    creator_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class SocietyMembers(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='society_members')
    society = models.ForeignKey(Society, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.society} - {self.user}'


class SocietyComments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    comment = models.CharField(max_length=230)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.society} - {self.user} - {self.comment}'
