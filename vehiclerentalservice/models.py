# from django.db import models

# class VehicleManager(models.Manager):
#     def create_vehicle(self, title, manufactured_date):
#         vehicle = self.create(title=title, manufactured_date=manufactured_date)
#         return vehicle

# # Create your models here.
# class Vehicle(models.Model):
#     title = models.CharField(max_length=255)
#     manufactured_date = models.DateField()

#     def __str__(self):
#         return self.title
    
#     objects = VehicleManager() 

# models.py
from django.db import models

# Vehicle model to represent a rental vehicle
class Vehicle(models.Model):
    name = models.CharField(max_length=100)  # Name of the vehicle
    type = models.CharField(max_length=50)   # Type of vehicle (e.g., Car, Bike, Truck)
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2)  # Daily rental price
    available = models.BooleanField(default=True)  # Whether the vehicle is available for rent

    def __str__(self):
        return self.name