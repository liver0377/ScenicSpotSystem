from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    ORDER_STATUS = (
        ('r', "ready to pay"),
        ('p', "paid"),
    )

    name = models.CharField(max_length=50) 
    status = models.CharField(max_length=30, choices=ORDER_STATUS)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    

class Ticket(models.Model):
    name = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, related_name="tickets", on_delete=models.CASCADE)

