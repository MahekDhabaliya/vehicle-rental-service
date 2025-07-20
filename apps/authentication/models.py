from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = [
        ('customer', 'Customer'),
        ('owner', 'Vehicle Owner'),
        ('admin', 'Platform Admin'),
        ('fleet_manager', 'Fleet Manager'),
        ('support', 'Support Agent'),
    ]
    
    phone = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=20, choices=ROLES, default='customer')
    is_verified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profiles/', blank=True)
    license_image = models.ImageField(upload_to='licenses/', blank=True)
    id_document = models.ImageField(upload_to='documents/', blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)