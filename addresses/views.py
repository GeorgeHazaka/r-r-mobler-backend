from rest_framework import generics, permissions, filters
from .models import Address
from .serializers import AddressSerializer
from rest_framework.permissions import IsAuthenticated


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'country',
        'state',
        'postal_code',
    ]
    ordering_fields = [
        'city',
        'state',
        'postal_code',
        'country',
        'created_at',
    ]

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
