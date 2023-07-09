from django.shortcuts import render
from .models import Article


# Create your views here.
def show_news(request):
    articles = Article.objects.all()
    return render(request, "news.html", { "articles": articles })

def news_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, "news_detail.html", { "article": article })
