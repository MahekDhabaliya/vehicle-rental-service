from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    vehicle_title = serializers.CharField(source='vehicle.title', read_only=True)
    renter_name = serializers.CharField(source='renter.username', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'renter', 'renter_name', 'vehicle', 'vehicle_title', 
                 'start_time', 'end_time', 'total_amount', 'deposit_amount', 
                 'status', 'payment_id', 'created_at']
        read_only_fields = ['id', 'created_at']