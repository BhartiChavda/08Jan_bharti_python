from django.contrib import admin
from django.urls import path,include
from tempintapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('errorpage/',views.errorpage),
    path('product/',views.product),
    path('team/',views.team),
    path('testimonial/',views.testimonial),
    path('service/',views.service),

  
]