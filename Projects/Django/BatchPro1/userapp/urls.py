from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_note, name='upload_note'),
    path('write/', views.write_note, name='write_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('archive/<int:note_id>/', views.toggle_archive, name='toggle_archive'),
    path('share/<int:note_id>/', views.toggle_share, name='toggle_share'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('view/<int:note_id>/', views.user_view_note, name='user_view_note'),
    path('settings/', views.settings, name='settings'),
    path('security/', views.security_settings, name='security_settings'),
    path('integrations/', views.integrations_settings, name='integrations_settings'),
    path('shared/view/<int:note_id>/', views.view_shared_note, name='view_shared_note'),

    # Password Reset URLs
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='userapp/password_reset.html'), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='userapp/password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='userapp/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='userapp/password_reset_complete.html'), 
         name='password_reset_complete'),
]
