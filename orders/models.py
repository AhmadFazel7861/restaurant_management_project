from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return super().get_queryset().filter(
            status__name__in=['pending', 'processing']
        )

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
    
    all_objects = models.Manager()
    
    objects = ActiveOrderManager()

    def __str__(self):
        return f"Order {self.id} - {self.customer_name} ({self.status})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} ({self.quantity})" 

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_until = models.DateField()

    def __str__ (self):
        return f"{self.code} - {self.discount_percentage}%"

        


