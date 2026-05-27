from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('profile/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.patient_registration, name='patient_registration'),
    path('payment/', views.payment, name='payment'),
    path('map/', views.map_view, name='map_view'),
    
    # AJAX endpoints
    path('api/doctors/', views.doctor_ajax_list, name='api_doctor_list'),
    path('api/doctors/add/', views.doctor_ajax_add, name='api_doctor_add'),
    path('api/doctors/delete/<int:doctor_id>/', views.doctor_ajax_delete, name='api_doctor_delete'),
]
