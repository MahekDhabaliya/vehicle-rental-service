from rest_framework import serializers
from .models import Dispute

class DisputeSerializer(serializers.ModelSerializer):
    reporter_name = serializers.CharField(source='reporter.username', read_only=True)
    
    class Meta:
        model = Dispute
        fields = ['id', 'booking', 'reporter', 'reporter_name', 'reported_user', 
                 'title', 'description', 'status', 'evidence_image', 'resolution', 
                 'created_at', 'resolved_at']
        read_only_fields = ['id', 'created_at']