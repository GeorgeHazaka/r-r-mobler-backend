from rest_framework import generics, permissions
from .models import OrderItem
from .serializers import OrderItemSerializer

class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Assuming the user has only one order for simplicity
        # You need to replace this logic with appropriate logic to select the correct order
        order = self.request.user.orders.first()
        serializer.save(order=order)

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user)
