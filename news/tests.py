from django.urls import reverse, resolve
from django.test import TestCase
from django.test import TestCase
from .models import Article
from . import views


# Create your tests here.
class NewsTest(TestCase):
    def setUp(self):
        Article.objects.create(
            title="xxx_title",
            content="xxx",
            image="xxx",
        )
        self.url_news = reverse("show_news")
        self.url_news_detail = reverse("news_detail", kwargs={"article_id": 1})

    def test_view_news(self):
        view = resolve(self.url_news)
        self.assertEquals(view.func, views.show_news)

    def test_news(self):
        response = self.client.get(self.url_news)
        self.assertEquals(response.status_code, 200)

    def test_view_news_detail(self):
        view = resolve(self.url_news_detail)
        self.assertEquals(view.func, views.news_detail)
    
    def test_news_detail(self):
        response = self.client.get(self.url_news_detail)
        self.assertEquals(response.status_code, 200)
