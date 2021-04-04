from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list_view, name='tweet-list'),
    path('<int:id>/', views.tweet_detail_view, name='tweet-detail'),
]
