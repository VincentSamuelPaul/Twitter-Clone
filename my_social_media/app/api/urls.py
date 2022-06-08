from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('tweets/', views.getTweets, name='getTweets'),
    path('gettweetuser/<int:tweet_user>/', views.getTweetUser, name='getTweetUser'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('getfollowerstweets', views.getFollowersTweets, name='getFollowersTweets'),
    path('addlikes/<int:tweet_id>', views.addLikes, name='addLikes'),
    path('subtractlikes/<int:tweet_id>', views.subtractLikes, name='subtractLikes'),
]