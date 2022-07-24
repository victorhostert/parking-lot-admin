from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class CustomerVehicle(models.Model):
    KIND_CHOICES = [
        (1, 'motorcycle'),
        (2, 'car')
    ]

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    plate = models.CharField(max_length=10)
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)

    def __str__(self) -> str:
        return f'Plate: {self.plate} - Customer: {self.customer}'