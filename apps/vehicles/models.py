from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('truck', 'Truck'),
        ('van', 'Van'),
    ]
    OWNER_TYPES = [
        ('platform', 'Platform Owned'),
        ('peer', 'Peer Owned'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Under Maintenance'),
        ('pending_approval', 'Pending Approval'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    owner_type = models.CharField(max_length=20, choices=OWNER_TYPES)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_vehicles')
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    registration_number = models.CharField(max_length=50, unique=True)
    manufactured_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='vehicles/', blank=True)
    insurance_document = models.ImageField(upload_to='insurance/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.registration_number}"