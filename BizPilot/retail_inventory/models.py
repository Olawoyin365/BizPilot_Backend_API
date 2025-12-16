from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    """
    Product-level category.
    Examples (Retail): -Toiletries, -Beverages, -Electronics
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Inventory product managed by a business owner
    """
    name = models.CharField(max_length=100)  # Product name
    sku = models.CharField(max_length=50, unique=True)  # Stock Keeping Unit
    description = models.TextField(blank=True)  # Product Desription
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Selling price
    quantity = models.IntegerField()  # Stock quantity
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # Product Category
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')  # Business owner who owns this product
    created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Update timestamp

    def __str__(self):
        return self.name
