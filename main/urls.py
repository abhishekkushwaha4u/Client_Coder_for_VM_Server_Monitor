from django.urls import path 
from . import views

urlpatterns = [
    path('check/health/', views.HealthCheckView.as_view()),
    path('choices/', views.AvailableSystemMonitoringChoices.as_view()),
    path('data/', views.ReturningSystemDataView.as_view()),
]