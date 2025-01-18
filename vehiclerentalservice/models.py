from django.db import models

class VehicleManager(models.Manager):
    def create_vehicle(self, title, manufactured_date):
        vehicle = self.create(title=title, manufactured_date=manufactured_date)
        return vehicle

# Create your models here.
class Vehicle(models.Model):
    title = models.CharField(max_length=255)
    manufactured_date = models.DateField()

    def __str__(self):
        return self.title
    
    objects = VehicleManager() 