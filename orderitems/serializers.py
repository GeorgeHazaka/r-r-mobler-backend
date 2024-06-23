from rest_framework import serializers
from .models import OrderItem
from products.models import Product
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)
    owner = serializers.ReadOnlyField(source='order.user.username')

    class Meta:
        model = OrderItem
        fields = [
            'id', 'owner', 'order', 'product',
            'product_id', 'quantity', 'price',
            'created_at', 'updated_at', 'owner'
        ]
        read_only_fields = ['order', 'price', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        price = product.price * quantity  # Calculate the price based on product price and quantity
        order_item = OrderItem.objects.create(price=price, **validated_data)
        return order_item
