from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('create/', views.create_service_request, name='create_request'),
    path('<int:pk>/', views.request_detail, name='request_detail'),
]