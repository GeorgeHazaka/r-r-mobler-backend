from django.urls import path
from cartitems import views

urlpatterns = [
    path('cartitems/', views.CartItemList.as_view(), name='cartitem-list'),
    path('cartitems/<int:pk>/', views.CartItemDetail.as_view(), name='cartitem-detail'),
]
