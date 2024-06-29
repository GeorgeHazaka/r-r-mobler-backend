from rest_framework import generics, permissions, filters
from .models import Cart
from .serializers import CartSerializer


class CartList(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'created_at',
    ]

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
