from django.test import TestCase
from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Order, OrderStatus
from . import views


# Create your tests here.
class UniPaymentTests(TestCase):
    def setUp(self):
        self.url_alipay = reverse("alipay")
        self.url_shop_result = reverse("shop_result")
        self.user = User.objects.create(username="xiaowang", email="xiaowang@gmail.com", password="123") 
        self.order = Order.objects.create(name="Order#1", status=OrderStatus.NOT_PAID, user=self.user)

    def test_view_alipay(self):
        view = resolve(self.url_alipay)
        self.assertEquals(view.func, views.alipay)

    def test_alipay(self):
        response = self.client.get(self.url_alipay, {"order_id": 1})
    
        # 验证重定向状态码
        self.assertEqual(response.status_code, 302)
    


        
    
    
    

