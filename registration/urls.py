from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Landing page with "Register" button
    path('register/', views.register, name='register'),  # Registration form page
    path('thank_you/', views.thank_you, name='thank_you'),  # Thank-you page after registration
]
