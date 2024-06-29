from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])

    def __str__(self):
        return f"{self.amount} - {self.user.username} - {self.product.name}"
