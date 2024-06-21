from django.urls import path
from addresses import views

urlpatterns = [
  path('addresses/', views.AddressList.as_view(), name='address-list'),
  path('addresses/<int:pk>/', views.AddressDetail.as_view(), name='address-detail'),
]
