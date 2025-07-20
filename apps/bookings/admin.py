from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'renter', 'vehicle', 'status', 'start_time', 'total_amount']
    list_filter = ['status', 'created_at']