from django.urls import reverse, resolve
from django.test import TestCase
from .models import Province, ScenicSpot
from . import views


class IntroductionTests(TestCase):
    def setUp(self):
        liaoning = Province.objects.create(name="辽宁")
        self.scenic_spot = ScenicSpot.objects.create(
            name="星海广场",
            description="xxx",
            ticket_price=20,
            image="scenic_spots/example.jgp",
            province=liaoning,
        )
        self.url_home = reverse("home")
        self.url_province = reverse(
            "province_spots", kwargs={"province_name": "辽宁"}
        )

    def test_view_home(self):
        view = resolve(self.url_home)
        self.assertEquals(view.func, views.home)

    def test_home(self):
        response = self.client.get(self.url_home)
        self.assertEquals(response.status_code, 200)

    def test_view_province(self):
        view = resolve(self.url_province)
        self.assertEquals(view.func, views.province_spots)

    def test_province(self):
        response = self.client.get(self.url_province)
        self.assertEquals(response.status_code, 200)


class IntroductionInvalidTests(TestCase):
    def setUp(self):
        self.url_home = reverse("home")
        self.url_province = reverse(
            "province_spots", kwargs={"province_name": "辽宁"}
        )
    
    def test_home(self):
        response = self.client.get(self.url_home)
        self.assertContains(response, "Province not found.")
    
    def test_province(self):
        response = self.client.get(self.url_province)
        self.assertContains(response, "Province not found.")
