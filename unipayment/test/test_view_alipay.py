from django.shortcuts import  reverse, redirect
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User
from ..views import alipay
from accounts.models import Order, Ticket, OrderStatus
from introduction.models import ScenicSpot, Province

class AliPayTests(TestCase):
    def setUp(self):
       self.url = reverse("alipay") 
       self.user = User.objects.create(username="xiaowang", email="xiaowang@gmail.com", password="123") 
       self.order = Order.objects.create(name="Order#1", status=OrderStatus.PAID, user=self.user)

       liaoning = Province.objects.create(name="辽宁")
       self.scenic_spot = ScenicSpot.objects.create(
           name="星海广场",
           description="xxx",
           ticket_price=20,
           image="scenic_spots/example.jgp",
           province=liaoning
       )

       ticket1 = Ticket.objects.create(name="星海广场门票", scenic_spot=self.scenic_spot, order=self.order)
       ticket2 = Ticket.objects.create(name="金沙滩门票", scenic_spot=self.scenic_spot, order=self.order)
    
    def test_view_order_pay(self):
        """
        测试订单支付的视图函数是否正确
        """
        view = resolve(self.url)
        self.assertEquals(view.func, alipay)
      
    # def test_valid_order_pay(self):
    #      response = self.client.get(self.url, { "order_id": self.order.pk }, follow=True)
    #      # print("order_id: {}".format(self.order.pk))
    #      self.assertEquals(response.status_code, 200)
