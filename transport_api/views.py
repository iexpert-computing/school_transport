# transport_api/views.py
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rolepermissions.checkers import has_role
from .serializers import (
    UserRegistrationSerializer, 
    UserSerializer, 
    VehicleSerializer
)
from .models import Vehicle

User = get_user_model()

# Permissão customizada para verificar se o usuário possui role 'admin'
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and has_role(request.user, 'admin')

# Endpoint para registro de novos usuários
class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# Endpoint para listar todos os usuários (acessível apenas a admins)
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

# Endpoint para listar e criar veículos
class VehicleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Verifica se o usuário é admin antes de permitir a criação
        if not has_role(self.request.user, 'admin'):
            raise permissions.PermissionDenied("You do not have permission to create a vehicle.")
        serializer.save()

# Endpoint para recuperar, atualizar e deletar um veículo específico
class VehicleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        if not has_role(request.user, 'admin'):
            raise permissions.PermissionDenied("You do not have permission to update this vehicle.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not has_role(request.user, 'admin'):
            raise permissions.PermissionDenied("You do not have permission to delete this vehicle.")
        return super().destroy(request, *args, **kwargs)
