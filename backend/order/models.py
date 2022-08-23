from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    OrderStatus = (
        ('Pending','Pending'),
        ('Dispatched','Dispatched'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Orders")
    date_time = models.DateTimeField(auto_created=True)
    status = models.CharField(max_length=60,choices=OrderStatus,default="Pending")
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    

class OrderDetails(models.Model):
        order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="OrderDetails")
        product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Product")
        quantity = models.IntegerField(default=1)
        price = models.DecimalField(max_digits=8,decimal_places=2)


        def __str__(self):
            return str(self.order)
        

