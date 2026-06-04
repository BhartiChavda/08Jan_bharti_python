from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('explore/', views.search, name='explore'),
    path('notifications/', views.notifications, name='notifications'),
    path('messages/', views.messages, name='messages'),
    path('post/', views.post_tweet, name='post_tweet'),
]
