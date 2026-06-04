from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment/', views.order_payment, name='payment'),
    path('success/', views.payment_success, name='success'),
]
