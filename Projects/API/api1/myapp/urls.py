from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path("",views.apidata),
   path("apiget/<int:id>/",views.apiget),
   path("apipost/",views.apipost),
   path("apidelete/<int:id>/",views.apidelete),
   path("apiupdate/<int:id>/",views.apiupdate),
 

]