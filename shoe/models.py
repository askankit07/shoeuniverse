from django.db import models
from django.utils import timezone
import uuid

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254 ,unique=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.email
    
class Order(models.Model):
    foreignKey=models.ForeignKey(Customer,on_delete=models.CASCADE)
    orderId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productId=models.CharField(max_length=36)
    productName=models.CharField(max_length=100)
    productQty=models.IntegerField()
    totalAmount=models.IntegerField()
    imageUrl = models.URLField(default=None)
    order_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.productName
    
class Cart(models.Model):
    foreignKey=models.ForeignKey(Customer,on_delete=models.CASCADE)
    CartId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    productId=models.CharField(max_length=36)
    productName=models.CharField(max_length=100)
    Amount=models.IntegerField()
    description = models.TextField(default=None)
    imageUrl = models.URLField(default=None)
   
    def __str__(self):
        return self.productName
    