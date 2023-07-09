from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from introduction.models import Province
from ..models import ScenicSpot


class AccountCardTests(TestCase):
    def setUp(self):
        self.url_login = reverse("login")
        self.user_data = {
            "username": "john",
            "email": "john@doe.com",
            "password": "gehigeqogngniqo123413",
        }
        self.user = User.objects.create(**self.user_data)
        self.province = Province.objects.create(name="Test Province")
        self.scenic_spot = ScenicSpot.objects.create(
            name="Test Scenic Spot",
            description="Test description",
            ticket_price=100.00,
            image="path/to/image.jpg",
            province=self.province,
        )
        self.login_response = self.client.post(
            self.url_login, {"username": "john", "password": "gehigeqogngniqo123413"}
        )

#     def test_account_card(self):
#         url_account_card = reverse("account_card", kwargs={"card_name": "orders"})
# 
#         response = self.client.get(url_account_card)
#         self.assertEquals(response.status_code, 200)
# 
#         response = self.client.get(url_account_card)
#         self.assertEquals(response.status_code, 200)
# 
#         url_account_card = reverse("account_card", kwargs={"card_name": "xxx"})
#         response = self.client.get(url_account_card)
#         self.assertEquals(response.status_code, 404)

#     def test_add_ticket_to_order(self):
#         # 创建新订单
#         url_add_ticket_to_order = reverse("add_ticket_to_order", kwargs={"spot_id": 1})
#         response = self.client.get(url_add_ticket_to_order)
#         self.assertEquals(response.status_code, 200)
# 
#         # 找到已经存在的订单
#         url_add_ticket_to_order = reverse("add_ticket_to_order", kwargs={"spot_id": 1})
#         response = self.client.get(url_add_ticket_to_order)
#         self.assertEquals(response.status_code, 200)
