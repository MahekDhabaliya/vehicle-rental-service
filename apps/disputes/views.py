from rest_framework import generics, permissions
from django.db.models import Q
from .models import Dispute
from .serializers import DisputeSerializer

class DisputeListCreateView(generics.ListCreateAPIView):
    serializer_class = DisputeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Dispute.objects.filter(
            Q(reporter=self.request.user) | Q(reported_user=self.request.user)
        )
    
    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)