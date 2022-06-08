from rest_framework.serializers import ModelSerializer

from app.models import Tweet, Followers
from django.contrib.auth.models import User


class TweetSerilizer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'

class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FollowerSerilizer(ModelSerializer):
    class Meta:
        model = Followers
        fields = '__all__'