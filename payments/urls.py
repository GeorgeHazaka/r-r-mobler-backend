from django.urls import path
from payments import views

urlpatterns = [
    path('payments/', views.PaymentList.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentDetail.as_view(), name='payment-detail'),
]
