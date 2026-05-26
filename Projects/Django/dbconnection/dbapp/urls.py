from django.contrib import admin
from django.urls import path, include
from dbapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('showdata/', views.showdata, name='showdata'),
    path('deletedata/<int:id>/', views.deletedata, name='deletedata'),  
    path('updatedata/<int:id>/', views.updatedata, name='updatedata'),  
]