from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login", views.login, name = 'login'),
    path("signup", views.signup, name = 'signup'),
    path("logout", views.logout, name = 'logout'),
   
#    password reset urls

   path('reset_password/',auth_views.PasswordResetView.as_view(template_name="account/password_rest_form.html"),name='reset_password'),

   path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),name='password_reset_done'),

   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"),name='password_reset_confirm'),

   path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),name='password_reset_complete'),

    ]