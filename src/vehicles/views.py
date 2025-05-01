from ast import Is

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser

from core.permissions import IsOwnerOfVehicleOrRecord
from .filters import VehicleFilterClass, VehicleTypeFilterClass
from .models import Vehicle, VehicleType
from .serializers import VehicleSerializer, VehicleTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    rql_filter_class = VehicleFilterClass
    permission_classes = [DjangoModelPermissions]


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    rql_filter_class = VehicleTypeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
