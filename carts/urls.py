from django.urls import path
from carts import views

urlpatterns = [
    path('carts/', views.CartList.as_view(), name='carts-list'),
    path('carts/<int:pk>/', views.CartDetail.as_view(), name='carts-detail'),
]
