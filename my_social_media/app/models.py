from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    tweet = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.tweet

class Followers(models.Model):
    main = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_user')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_of_main')

    def __str__(self):
        return (f'{self.follower} follows {self.main}')