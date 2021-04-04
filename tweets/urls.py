from django.urls import path
from .views import tweet_detail_view, tweet_list_view, tweets_view

urlpatterns = [
    path('', tweets_view, name='tweets'),
    path('list/', tweet_list_view, name='tweet-list'),
    path('<int:id>/', tweet_detail_view, name='tweet-detail'),
]
