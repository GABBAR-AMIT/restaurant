from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    item_name=models.CharField(max_length=25, unique=True)
    item_description=models.TextField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.item_name
    
class Order(models.Model):
    table_number = models.IntegerField()
    items = models.ManyToManyField(Menu, through='OrderItem')
    order_number = models.CharField(max_length=10, unique=True, default='N/A')
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Order {self.order_number} - Table {self.table_number}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)