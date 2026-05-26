from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home, name='home'),
    path('signup/',views.signup),
    path('userlogout/',views.userlogout),
]