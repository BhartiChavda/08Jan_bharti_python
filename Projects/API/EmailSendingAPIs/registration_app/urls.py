from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('otp-verify/', views.otp_verify, name='otp_verify'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
