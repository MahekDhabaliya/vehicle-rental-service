from rest_framework import generics, permissions
from django.db.models import Q
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Vehicle.objects.filter(status='available')
        vehicle_type = self.request.query_params.get('type')
        owner_type = self.request.query_params.get('owner_type')
        location = self.request.query_params.get('location')
        
        if vehicle_type:
            queryset = queryset.filter(vehicle_type=vehicle_type)
        if owner_type:
            queryset = queryset.filter(owner_type=owner_type)
        if location:
            queryset = queryset.filter(location__icontains=location)
            
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Vehicle.objects.all()

class MyVehiclesView(generics.ListAPIView):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)