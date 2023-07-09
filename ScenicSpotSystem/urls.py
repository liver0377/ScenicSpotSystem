"""
URL configuration for ScenicSpotSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from introduction import views as introduction_views
from django.conf import settings
from django.conf.urls.static import static
from unipayment import views as uni_views 
from news import views as news_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path("", introduction_views.home, name="home"),

    path("signup/", accounts_views.signup, name="signup"),

   # 使用django官方的LogoutView
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # 使用django官方的LoginView
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),

    path("account/<str:card_name>/", accounts_views.account_card, name="account_card"),

    path("introduction/scenicspot/<str:province_name>/", introduction_views.province_spots, name="province_spots"),

    path("shop/alipay/", uni_views.alipay, name="alipay"),

    # 用户点击"加入订单", 触发该路由
    path("add_ticket_to_order/<int:spot_id>/", accounts_views.add_ticket_to_order, name="add_ticket_to_order"),

    path("shop/result/", uni_views.shop_result, name="shop_result"),

    path("news/<int:article_id>/", news_views.news_detail, name="news_detail"),

    path("news/", news_views.show_news, name="show_news"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
