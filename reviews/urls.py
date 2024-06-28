from django.urls import path
from reviews import views

urlpatterns = [
    path('products/<int:product_id>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('products/<int:product_id>/reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]
