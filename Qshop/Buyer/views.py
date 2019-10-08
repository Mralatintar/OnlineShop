# # from django.shortcuts import render,HttpResponseRedirect
# from django.shortcuts import render, HttpResponseRedirect,render_to_response
# from django.core.paginator import Paginator
# from Buyer.models import *
# import hashlib
# from django.http import JsonResponse
# from Seller.models import *
# from Seller.views import *


from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from Seller.models import *
from Seller.views import setPassword
from Buyer.models import *
from alipay import AliPay

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_user=request.COOKIES.get("username")
        session_user=request.session.get("username")
        if cookie_user and session_user and cookie_user==session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Buyer/login/")
    return inner

import logging
collect=logging.getLogger("django")

def login(request):                                             #登录页面
    if request.method=="POST":                                  #判断接口为post
        password=request.POST.get("pwd")                         #获取网页传来的pwd
        email=request.POST.get("email")                         #获取网页传来的email
        user=LoginUser.objects.filter(email=email).first()       #user存储 网页传来的email和数据库的email
        if user:                                                 #判断是否存在对应的user
            db_password=user.password                               #获取数据库对应用户的密码
            password=setPassword(password)                          #对页面传来的密码进行MD5加密
            if db_password==password:                               #如果两值相等
                response=HttpResponseRedirect("/Buyer/index/")      #跳转到index主页
                response.set_cookie("user_id",user.id)
                response.set_cookie("email",user.email)
                response.set_cookie("username",user.username)
                request.session["username"]=user.username
                collect.debug("%s is login"%user.username)
                return response
                # return HttpResponseRedirect("/Buyer/index/")
    return render(request,"buyer/login.html",locals())
def register(request):                                          #注册页面
    if request.method=="POST":                                  #如果接口方式是post
        username=request.POST.get("user_name")                  #获取页面name是user_name的值
        password=request.POST.get("pwd")                        #&
        email=request.POST.get("email")                         #&

        user=LoginUser()                                        #实例化对象表user
        user.username=username                                  #把username传入
        user.password = setPassword(password)                   #把password经过md5加密后传入
        user.email = email                                      #把email传入
        user.save()                                             #保存
        return HttpResponseRedirect("/Buyer/login/")          #返回到登录页面
    return render(request,"buyer/register.html")
def index(request):                                                 #主页
    goods_type=GoodsType.objects.all()                              #获取商品类型表内所有
    result=[]                                                       #给个result的空列表
    for ty in goods_type:                                  #对商品的类型进行循环给ty为单个类型
        goods=ty.goods_set.order_by("-goods_pro_time")    #yt对应的外键和表goods连接获取商品列表
        if len(goods)>=4:                                 #如果商品数量大于4
            goods=goods[:4]                                #把前4个给goods
            result.append({"type":ty,"good_list":goods})    #把循环的单个类型和前4个商品给result
    return render(request,"buyer/index.html",locals())

def logout(request):                        #登出
    url=request.META.get("HTTP_REFERER","/Buyer/index/")#获取登出后获得的url
    response=HttpResponseRedirect(url)                  #返回结果并跳转到url
    for k in request.COOKIES:                           #循环COOKIES给k
        response.delete_cookie(k)                       #清除cookie
    del request.session["username"]                    #删除session的username
    return response                                     #返回到url


def goods_list(request):                                #商品列表
    request_type=request.GET.get("type")                #结束网页传来的type给request_type，搜索框搜索情况下type=k
    keyword=request.GET.get("keywords")                 #把keywords的值给keyword
    goods_list=[]                                       #创建空列表goods_list
    if request_type=="t":                               #如果请求为t，说明不在搜索也是在类型进行查询
        if keyword:                                     #如果keyword存在
            id=int(keyword)                              #转化为整型
            goods_type=GoodsType.objects.get(id=id)     #获取商品类型的id并且实例化
            goods_list=goods_type.goods_set.order_by("-goods_pro_time") #根据外键把对应商品类型的 商品数据排列
    elif request_type=="k":
        if keyword:
            goods_list=Goods.objects.filter(goods_name__contains=keyword).order_by("-goods_pro_time")
    if goods_list:                                      #如果存在数据
        lenth=len(goods_list)/5                         #进行分页  求整得到
        if lenth!=int(lenth):                          #如果不被5整除
            lenth+=1                                    #lenth加1
        lenth=int(lenth)                                #可以被5整除获得lenth
        recommend=goods_list[:lenth]                    #获得前lenth个数据
    return render(request,"buyer/goods_list.html",locals())



def goods_detail(request,id):                                   #商品的    详情页
    goods=Goods.objects.get(id=int(id))                         #根据传来的id来获取商品信息
    return render(request,"buyer/detail.html",locals())

@loginValid                                                 #装饰器判定是否存在cookie
def user_center_info(request):                              #用户个人中心
    return render(request,"buyer/user_center_info.html",locals())

import time                                                 #引入time模块
import datetime                                             #引入模块

@loginValid
def pay_order_more(request):    #多个商品订单
    data=request.GET            #把结果返回给data
    data_item=data.items()      #把字典转换为列表包含元组，如{'a':1,'b',2}-->[('a',1),('b',2)]
    request_data=[]             #创建空列表
    for key,value in data_item: #遍历列表获取键和值
        if key.startswith("check_"):    #如果键以check_开头
            goods_id=key.split("_",1)[1]        #goods_id分割第一个_下划线，获取id
            count=data.get("count_"+goods_id)       #获取数量
            request_data.append((int(goods_id),int(count)))#加入列表
    if request_data:
        order=PayOrder()
        order.order_number=str(time.time()).replace(".","")
        order.order_data=datetime.datetime.now()
        # order.order_status=0
        order.order_user=LoginUser.objects.get(id=int(request.COOKIES.get("user_id")))
        order.save()
        order_total=0
        for goods_id,count in request_data:     #遍历列表[(key,value),(key,value),(key,value)]
            goods=Goods.objects.get(id=int(goods_id))
            order_info = OrderInfo()
            order_info.order_id = order
            order_info.goods_id = goods.id
            order_info.goods_status = 0
            order_info.goods_picture = goods.picture
            order_info.goods_name = goods.goods_name
            order_info.goods_count = int(count)
            order_info.goods_price = goods.goods_price
            order_info.goods_total_price = goods.goods_price * int(count)
            order_info.store_id = goods.goods_store  # 商品卖家，goods.goods_store本身就是一条卖家数据
            order_info.save()
            order_total+=order_info.goods_total_price
        order.order_total=order_total
        order.save()
    return render(request,"buyer/pay_order.html",locals())


from Qshop.settings import alipay_public_key_string,alipay_private_key_string



@loginValid
def add_cart(request):                          #加入到购物车的方法
    result={                                    #创建字典result
        "code":200,
        "data":""
    }
    if request.method=="POST":                 #如果请求方式是POST
        id=int(request.POST.get("goods_id"))   #获取请求商品的id
        count=int(request.POST.get("count",1))  #获取请求商品的数量，默认为1

        goods=Goods.objects.get(id=id)          #根据商品id实例化商品属性，
        cart=Cart()                             #实例化购物车表
        cart.goods_name=goods.goods_name        #保存到购物车的商品名称
        cart.goods_number=count
        cart.goods_price=goods.goods_price
        cart.goods_picture=goods.picture
        cart.goods_total=goods.goods_price*count    #商品总价
        cart.goods_id=id                            #购物车goods_id等于商品字段的值
        cart.cart_user=request.COOKIES.get("user_id") #购物车的cart_user字段和登录的用户id相等
        cart.save()                             #保存
        result["data"]="恭喜你,加入购物车成功"    #返回字典data:xx
    else:
        result["code"]=500
        result["data"]="抱歉,请求方式错误"
    return JsonResponse(result)    #把处理后的结果返回到页面{"code"200:,"data":成功}

def cart(request):                   #进入购物车后的页面
    user_id=request.COOKIES.get("user_id")         #获取COOKIE里的id给user_id
    goods=Cart.objects.filter(cart_user=int(user_id)).order_by("-id")    #筛选该用户在购物车列表内对应的商品列表并排序
    count=goods.count()            #获取加入购物车的商品数量
    return render(request,"buyer/cart.html",locals())
@loginValid
def user_center_order(request):
    user_id=request.COOKIES.get("user_id")
    user=LoginUser.objects.get(id=int(user_id))
    order_list=user.payorder_set.order_by("-order_data")
    bkb=user.orderinfo_set.order_by("-goods_status")
    return render(request,"buyer/user_center_order.html",locals())
# Create your views here.





def middle_test_view(request):
    print("I am view")
    # huqingjie+1
    return JsonResponse({"data":"hello world"})

from django.core.cache import cache
def cacheTest(request):
    user=cache.get("user")
    if not user:
        user=LoginUser.objects.get(id=1)
        cache.set("user",user,30)
    return JsonResponse({"data":"hellow world"})



# def ceshi(request):
#     goods_type = GoodsType.objects.all()
#     for i in goods_type:
#         xdd=i.picture
#         print(xdd)
#     return render(request,"buyer/ceshi.html",locals())