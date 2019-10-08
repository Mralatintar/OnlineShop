from django.contrib import admin
from django.urls import path,re_path,include
from Seller.views import *
from django.views.decorators.cache import cache_page
# from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',cache_page(60*11)(register)),
    path('login/',login),
    path('logout/',logout),

    path('personal_info/', personal_info),
    path('goods_add/', goods_add),
    path('slc/', send_login_code),
    path('change_order/',change_order),
    re_path(r'order_list/(?P<status>\d{1})', order_list),


    # path('vue_test/',vue_test),

    path('index/',index),
    re_path('goods_list/(?P<page>\d+)/(?P<status>[01])/',goods_list),
    re_path('goods_status/(?P<state>\w+)/(?P<id>\d+)',good_status),
    ]