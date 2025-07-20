from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    
    class Meta:
        model = Vehicle
        fields = ['id', 'title', 'description', 'vehicle_type', 'owner_type', 
                 'owner', 'owner_name', 'price_per_hour', 'location', 'latitude', 
                 'longitude', 'status', 'registration_number', 'manufactured_date', 
                 'rating', 'image', 'insurance_document', 'created_at']
        read_only_fields = ['id', 'rating', 'created_at']