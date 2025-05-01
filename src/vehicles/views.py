from ast import Is
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets
from core.permissions import IsOwnerOfVehicleOrRecord
from .models import Vehicle, VehicleType
from .serializers import VehicleSerializer, VehicleTypeSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions]

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser, IsOwnerOfVehicleOrRecord]
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
