from django.urls import path 
from . import views

urlpatterns = [
    path('check/health/', views.HealthCheckView.as_view()),
]