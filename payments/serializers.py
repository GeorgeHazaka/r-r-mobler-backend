from rest_framework import serializers
from .models import Payment
from products.models import Product

class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Payment
        fields = [
            'payment_id', 'user', 'product',
            'product_name', 'amount', 'transaction_id',
            'payment_date', 'status'
        ]
