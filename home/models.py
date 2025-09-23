from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
        
class MenuItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('MenuCategory', on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} (${self.price})"