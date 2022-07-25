from rest_framework import viewsets, permissions, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from customer.models import CustomerVehicle

from .models import ParkMovement
from .serializers import ParkMovementSerializer


class ParkMovementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parking lot movements to be created and updated
    """

    queryset = ParkMovement.objects.all()
    serializer_class = ParkMovementSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        plate = request.data['plate']
        vehicle = request.data['vehicle']
        if not vehicle:
            try:
                customer_vehicle = CustomerVehicle.objects.get(plate=plate)
                request.data['vehicle'] = customer_vehicle.id
            except Exception:
                pass
        return super().create(request, *args, **kwargs)
        

class ParkMovementExitViewSet(viewsets.ViewSet):
    """
    API endpoint that allows the addition of an exit_date to an existing parking lot movement
    """

    def movement_exit(self, request, *args, **kwargs):
        movement_id = request.data['movement_id']
        exit_date = request.data['exit_date']
        try:
            park_movement = ParkMovement.objects.get(id=movement_id)
            park_movement.exit_date = exit_date
            park_movement.save()
            return Response(data={'exit_date': exit_date}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'Error:': e}, status=status.HTTP_400_BAD_REQUEST)