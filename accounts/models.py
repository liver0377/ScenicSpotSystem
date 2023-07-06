from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

# Create your models here.
class OrderStatus(models.TextChoices):
    NOT_PAID = ('r', "ready to pay")
    PAID = ('p', "paid")

class Order(models.Model):

    name = models.CharField(max_length=50) 
    status = models.CharField(max_length=30, choices=OrderStatus.choices)
    purchase_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)

    def caculate_total_price(self):
        total_price = self.tickets.aggregate(total=Sum('unit_price')).get('total')
        return total_price 

class Ticket(models.Model):
    name = models.CharField(max_length=200)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, related_name="tickets", on_delete=models.CASCADE)

