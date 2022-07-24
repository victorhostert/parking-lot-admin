from rest_framework import viewsets
from rest_framework import permissions
from .models import CustomerVehicle, Customer
from .serializers import CustomerSerializer, CustomerVehicleSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be created and updated
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]


class CustomerVehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customer vehicles to be created and updated
    """

    queryset = CustomerVehicle.objects.all()
    serializer_class = CustomerVehicleSerializer
    permission_classes = [permissions.AllowAny]