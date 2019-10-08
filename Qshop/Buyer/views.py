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





