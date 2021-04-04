from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from .models import Tweet


def tweet_list_view(request):
    all_tweets = get_list_or_404(Tweet)
    
    return JsonResponse(data={"msg": "obtanied list !"})


def tweet_detail_view(request, id):
    return JsonResponse(data={"msg": "obtanied detail !"})
