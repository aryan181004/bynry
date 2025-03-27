from django.urls import path
from . import views

urlpatterns = [
    path('', views.support_dashboard, name='support_dashboard'),
    path('request/<int:pk>/', views.manage_request, name='manage_request'),
]