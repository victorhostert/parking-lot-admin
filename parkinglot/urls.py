from django.urls import include, path
from rest_framework import routers
from customer.views import CustomerViewSet, CustomerVehicleViewSet
from parkmovement.views import ParkMovementViewSet, ParkMovementExitViewSet

movement_exit = ParkMovementExitViewSet.as_view({
    'put': 'movement_exit'
})

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'vehicle', CustomerVehicleViewSet, basename='vehicle')
router.register(r'movement', ParkMovementViewSet, basename='movement')
router.register(r'movement_exit', ParkMovementExitViewSet, basename='movement_exit')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/movement_exit/', movement_exit),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]