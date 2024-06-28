from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating} stars for {self.product.name} by {self.user.username}"
