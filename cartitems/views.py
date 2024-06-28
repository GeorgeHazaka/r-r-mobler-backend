from rest_framework import generics, permissions
from .models import CartItem
from .serializers import CartItemSerializer
from products.models import Product
from carts.models import Cart


class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart_id = self.kwargs.get('cart_id')
        product_id = self.request.data.get('product')

        cart = Cart.objects.get(cart_id=cart_id, user=self.request.user)
        product = Product.objects.get(id=product_id)

        serializer.save(cart=cart, product=product)

    def get_queryset(self):
        cart_id = self.kwargs.get('cart_id')
        user = self.request.user
        return CartItem.objects.filter(cart__cart_id=cart_id, cart__user=user)


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        cart_id = self.kwargs.get('cart_id')
        user = self.request.user
        return CartItem.objects.filter(cart_id=cart_id, cart__user=user)
