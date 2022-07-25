from django.db import models

class ParkMovement(models.Model):
    entry_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)
    validate_date = models.DateField(null=True, blank=True)
    value = models.DecimalField(decimal_places=2, max_digits=255, null=True, blank=True)
    vehicle = models.ForeignKey('customer.CustomerVehicle', on_delete=models.CASCADE, null=True, blank=True)
    plate = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Entry: {self.entry_date} Plate: {self.vehicle.plate} Value: {self.value}'
