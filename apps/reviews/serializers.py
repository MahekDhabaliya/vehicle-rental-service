from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(source='reviewer.username', read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'booking', 'reviewer', 'reviewer_name', 'reviewee', 
                 'vehicle', 'review_type', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']