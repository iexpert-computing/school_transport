# transport_api/models.py
from django.db import models

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.model} ({self.license_plate})"
