from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from customers.filters import CustomFilterClass
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    rql_filter_class = CustomFilterClass
    permission_classes = [IsAdminUser, DjangoModelPermissions]
