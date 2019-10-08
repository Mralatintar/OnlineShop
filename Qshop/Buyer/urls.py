from django.contrib import admin
from django.urls import path,re_path,include
from Buyer.views import *

urlpatterns = [
    path('login/',login),
    path('index/',index),
    path('register/',register),
    path('logout/', logout),


    path('add_cart/', add_cart),
    path('cart/',cart),
    path('pay_order_more/', pay_order_more),
    path('uco/',user_center_order),
    path('mtv/',middle_test_view),
    # path('ceshi/', ceshi),



    path('pay_order/', pay_order),
    path('alipay/', alipayGo),
    path('pay_result/', pay_result),

    path('goods_list/', goods_list),
    path('user_center_info/', user_center_info),

    re_path('goods_detail/(?P<id>\d+)/', goods_detail),
    ]