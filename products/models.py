from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products') 
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    numReviews = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-createdAt']
