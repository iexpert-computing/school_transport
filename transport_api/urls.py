# transport_api/urls.py
from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserListAPIView,
    VehicleListCreateAPIView,
    VehicleRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('vehicles/', VehicleListCreateAPIView.as_view(), name='vehicle-list-create'),
    path('vehicles/<int:pk>/', VehicleRetrieveUpdateDestroyAPIView.as_view(), name='vehicle-detail'),
]
