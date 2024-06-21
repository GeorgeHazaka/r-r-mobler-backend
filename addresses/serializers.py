from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id', 'owner', 'address_line1', 'address_line2',
            'city', 'state', 'postal_code', 'country',
            'created_at', 'updated_at'
        ]
