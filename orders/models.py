from django.contrib.auth.models import User
from django.db import models
from addresses.models import Address


class Order(models.Model):
    owner = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    shipping_address = models.ForeignKey(Address, related_name='shipping_orders', on_delete=models.CASCADE)
    billing_address = models.ForeignKey(Address, related_name='billing_orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status
