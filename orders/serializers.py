from rest_framework import serializers
from .models import Order
from addresses.models import Address
from addresses.serializers import AddressSerializer

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 'owner', 'is_owner', 'order_date', 'total_amount', 'status',
            'shipping_address', 'billing_address', 'created_at', 'updated_at'
        ]
