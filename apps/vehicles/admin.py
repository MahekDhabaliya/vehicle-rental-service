from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['title', 'vehicle_type', 'owner_type', 'owner', 'status', 'price_per_hour']
    list_filter = ['vehicle_type', 'owner_type', 'status']
    search_fields = ['title', 'registration_number', 'location']