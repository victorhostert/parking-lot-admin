from rest_framework import serializers

from .models import ParkMovement

class ParkMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkMovement
        fields = '__all__'
