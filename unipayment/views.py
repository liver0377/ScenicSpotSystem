from django.shortcuts import redirect
from alipay.utils import AliPayConfig
from django.http import HttpResponse
from alipay import AliPay
from alipay.utils import AliPayConfig
from accounts.models import Order, OrderStatus, Ticket

import time
import random

from ScenicSpotSystem.settings import (
    ALIPAY_APP_ID,
    ALIPAY_PUBLIC_KEY_STRING,
    ALIPAY_SERVER_URL,
    ALIPAY_RETURN_URL,
    APP_PRIVATE_KEY_STRING,
)

def create_alipay_client():
    return AliPay(
        appid=ALIPAY_APP_ID,
        app_notify_url=None,
        app_private_key_string=APP_PRIVATE_KEY_STRING,
        alipay_public_key_string=ALIPAY_PUBLIC_KEY_STRING,
        sign_type="RSA2",
        debug=False,
        verbose=False,
        config=AliPayConfig(timeout=15),
    ) 


def alipay(request):
    """
    通过该函数向支付宝服务商提供订单, 效果是弹出账密页面
    支付成功之后, 跳转到ALIPAY_RETURN_URL
    """
    alipay_client = create_alipay_client() 



    order_id = request.GET.get('order_id')
    order = Order.objects.get(pk=order_id)
 
    order_string = alipay_client.api_alipay_trade_page_pay(
        out_trade_no = str(int(time.time())) + str(random.randint(1, 1000)), 
        total_amount=str(order.caculate_total_price()),
        subject=str(order.name),
        return_url=ALIPAY_RETURN_URL,
    )
    return redirect(ALIPAY_SERVER_URL + "?" + order_string)


def shop_result(request):
    if request.method == "GET":
        # 进行校验，因为支付成功之后，后端是不知道是否成功的，所以需要校验一下
        alipay_client = create_alipay_client() 
        data = request.GET.dict()  # 把get请求的参数转换成字典
        signature = data.pop("sign")  # 把sign pop出去
        # verification
        success = alipay_client.verify(data, signature)  # success ----> True False
        # 上面的都是固定用法
        if success:
            # 支付成功之后的逻辑
            
            # 创建ticket, order对象并写入数据库

            Order.objects.filter(status=OrderStatus.NOT_PAID).update(status=OrderStatus.PAID)

            return redirect("home")

        return HttpResponse("支付失败")
