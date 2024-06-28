from django.urls import path
from cartitems import views

urlpatterns = [
    path('carts/<int:cart_id>/items/', views.CartItemList.as_view(), name='cartitem-list'),
    path('carts/<int:cart_id>/items/<int:product_id>/', views.CartItemDetail.as_view(), name='cartitem-detail'),
]
