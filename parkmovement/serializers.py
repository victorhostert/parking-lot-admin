from rest_framework import serializers

from .models import ParkMovement

class ParkMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkMovement
        fields = '__all__'

    def validate(self, data):
        """
        Checks if the exit_date comes after the entry_date
        Checks if there's a validated date before the exit
        """
        if data['entry_date'] > data['exit_date']:
            raise serializers.ValidationError({"exit_date": "exit date must be posterior to entry_date"})
        if not data['validate_date']:
            raise serializers.ValidationError({"exit_date": "must have validated date before the exit_date"})
        if data['value'] and not data['validate_date']:
            raise serializers.ValidationError({"value": "you can only add a value if you have a validate_date"})
        if data['validate_date'] and not data['value']:
            raise serializers.ValidationError({"validate_date": "you can only add a validate_date if you have a value"})
        return data