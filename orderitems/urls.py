from django.urls import path
from orderitems import views

urlpatterns = [
  path('orderitems/', views.OrderItemList.as_view(), name='orderitem-list'),
  path('orderitems/<int:pk>/', views.OrderItemDetail.as_view(), name='orderitem-detail'),
]
