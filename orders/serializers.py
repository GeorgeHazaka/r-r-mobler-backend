from rest_framework import serializers
from .models import Order
from addresses.models import Address
from addresses.serializers import AddressSerializer

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    shipping_address = AddressSerializer(read_only=True)
    billing_address = AddressSerializer(read_only=True)
    shipping_address_id = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(), source='shipping_address', write_only=True)
    billing_address_id = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(), source='billing_address', write_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'is_owner', 'order_date', 'total_amount', 'status',
            'shipping_address', 'billing_address', 'shipping_address_id',
            'billing_address_id', 'created_at', 'updated_at'
        ]
