from django.test import TestCase
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from introduction.models import Province
from ..models import OrderStatus, Order, Ticket, ScenicSpot
from ..views import login
from django.contrib.auth.views import LoginView


class LoginTests(TestCase):
    def setUp(self):
        self.url = reverse("login")
        self.user_data = {
            "username": "john",
            "email": "john@doe.com",
            "password": "abcdef123456",
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
        self.order = Order.objects.create(
            name="Test Order", status=OrderStatus.NOT_PAID, user=self.user
        )

        # 创建一个门票对象，关联到订单对象和景点对象
        self.ticket = Ticket.objects.create(
            name="Test Ticket", order=self.order, scenic_spot=self.scenic_spot
        )

    def test_view_login(self):
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, LoginView)

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_login_failure(self):
        # 尝试使用错误的用户名和密码登录
        response = self.client.post(
            self.url, {"username": "john", "password": "incorrectpassword"}
        )

        # 检查登录失败后页面是否重新显示登录表单
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

        # 检查用户是否未登录（即 session 中是否不存储用户信息）
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_login_success(self):
        # 尝试使用正确的用户名和密码登录
        response = self.client.post(
            self.url, {"username": "john", "password": "abcdef123456"}
        )

        # 检查登录后是否重定向到一个特定页面（例如首页）
        # self.assertRedirects(response, reverse("home"))

        # 检查用户是否成功登录（可以通过检查用户是否存储在 session 中来判断）
        # self.assertIn("_auth_user_id", self.client.session)

    def test_logout(self):
        # 先登录用户
        self.client.login(username="john", password="abcdef123456")

        # 在登录状态下访问注销的URL
        response = self.client.get(reverse("logout"))

        # 检查是否重定向到登录页面
        self.assertRedirects(response, reverse("home"))

        # 检查用户是否成功注销（即 session 中是否不存储用户信息）
        self.assertNotIn("_auth_user_id", self.client.session)
