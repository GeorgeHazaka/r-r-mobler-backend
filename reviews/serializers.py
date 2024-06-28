from rest_framework import serializers
from .models import Review
from products.models import Product


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Review
        fields = ['review_id', 'user', 'product', 'product_name', 'rating', 'comment', 'created_at', 'updated_at']
