from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'user', 'amount', 'payment_type', 'status', 
                 'gateway_transaction_id', 'created_at']
        read_only_fields = ['id', 'created_at']