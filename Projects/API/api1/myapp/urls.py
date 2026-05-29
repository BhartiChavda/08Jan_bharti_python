from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   
   #2nd try
   path("",views.data),
   path("data/",views.data),
   path("specified/<int:id>/",views.specified),
   path("de/<int:id>/",views.de),
   path("up/<int:id>/",views.up),
 ] 
"""path("",views.apidata),
   path("apiget/<int:id>/",views.apiget),
   path("apipost/",views.apipost),
   path("apidelete/<int:id>/",views.apidelete),
   path("apiupdate/<int:id>/",views.apiupdate),"""