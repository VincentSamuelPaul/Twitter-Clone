from django.http import JsonResponse
from django.shortcuts import render
from itsdangerous import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TweetSerilizer, UserSerilizer, FollowerSerilizer
from app.models import Tweet, Followers
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTweets(request):
    user_id = request.user
    username = User.objects.filter(username=user_id).only('id')
    tweets = Tweet.objects.filter(user=user_id)
    serializer = TweetSerilizer(tweets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFollowersTweets(request):
    user_id = 'Vincent'
    username = User.objects.filter(username=user_id).values_list('id')
    followers = Followers.objects.filter(main_id=username[0][0]).values_list('follower_id')
    z = []
    for x in followers:
        for y in x:
            if y != []:
                tweets = Tweet.objects.filter(user=y).values()
                z.append(tweets)
    serializer = TweetSerilizer(z, many=True)
    return Response(z)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTweetUser(request, tweet_user):
    tweet_user = User.objects.get(id=tweet_user)
    username = tweet_user.username
    return Response(username)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def addLikes(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    print(tweet.likes)
    tweet.likes += 1
    tweet.save()
    serializer = TweetSerilizer(tweet, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subtractLikes(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    print(tweet.likes)
    tweet.likes -= 1
    tweet.save()
    serializer = TweetSerilizer(tweet, many=False)
    return Response(serializer.data)