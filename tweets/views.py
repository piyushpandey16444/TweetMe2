from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from .serializers import TweetSerializer
from .models import Tweet
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def tweets_view(request):
    all_tweets = get_list_or_404(Tweet)
    return render(request, 'pages/home.html', context={'tweets': all_tweets})


@csrf_exempt
def tweet_list_view(request):
    """
    REST API view for all tweets.
    """
    all_tweets = get_list_or_404(Tweet)
    serializer = TweetSerializer(all_tweets, many=True)
    return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)


@csrf_exempt
def tweet_detail_view(request, id):
    """
    REST API view for single tweet.
    """
    tweet_obj = get_object_or_404(Tweet, id=id)
    serializer = TweetSerializer(tweet_obj)
    return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
