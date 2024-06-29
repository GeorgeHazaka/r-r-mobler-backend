from rest_framework import generics, filters
from rrmobler.permissions import IsAdminUserOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'name',
        'category__name',
    ]
    ordering_fields = [
        'name',
        'category',
        'price',
        'stock_quantity',
        'created_at',
    ]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]


# def search(request):
#     query = request.GET.get('q')
#     products = Product.objects.filter(
#         Q(name__icontains=query) |
#         Q(description__icontains=query) |
#         Q(category__name__icontains=query)
#     ) if query else Product.objects.none()
#     context = {
#         'products': products,
#     }
#     return render(request, 'search_results.html', context)
