from django.shortcuts import render, HttpResponseRedirect,render_to_response,HttpResponse
from Seller.models import *
import hashlib
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt    #免除csrf保护
from django.http import JsonResponse

def setPassword(password):                  #对密码进行加密
    md5=hashlib.md5()                       #实例化md5方法
    md5.update(password.encode())           #对传入的password进行加密
    result=md5.hexdigest()                  #加密后返回结果给result
    return result
def register(request):
    error_message=""
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        # username = request.POST.get("username")
        # age = request.POST.get("age")
        # gender = request.POST.get("gender")
        # address = request.POST.get("address")
        # phone_number = request.POST.get("phone_number")
        # photo=request.POST.get("photo")
        if email:
            user=LoginUser.objects.filter(email=email).first()
            if not user:
                new_user=LoginUser()
                new_user.email=email
                # new_user.username=username
                new_user.password=setPassword(password)
                # new_user.age=age
                # new_user.gender=gender
                # new_user.address=address
                # new_user.phone_number=phone_number
                # new_user.photo=photo
                new_user.save()
            else:
                error_message="邮箱已经被注册，请登录"
        else:
            error_message="邮箱不可为空"


    return render(request, "seller/register.html", locals())

def loginValid(fun):#装饰器
    def inner(request,*args,**kwargs):
        # cookie_username=request.COOKIES.get("username")
        # session_username=request.session.get("username")
        # if cookie_username and session_username and session_username==cookie_username:
        cookie_email = request.COOKIES.get("email")                         #提取本地缓存的cookie的email
        session_email = request.session.get("email")                        #提取服务器端的email
        if cookie_email and session_email and session_email == cookie_email:#如果都不为空而且都相等
            return fun(request,*args,**kwargs)                              #执行装饰器
        else:
            return HttpResponseRedirect("/login/")                          #否则跳转到login
    return inner

@loginValid
def index(request):
    return render(request,"seller/index.html",locals())


# 登录
import time
import datetime
from django.views.decorators.cache import cache_page
@cache_page(60*15)
def login(request):
    error_message=""                 #异常状态容器
    if request.method=="POST":      #如果请求是post
        email=request.POST.get("email")     #email等于post请求传过来的name=email值
        password=request.POST.get("password")   #password等于post请求传过来的name=password的值
        code=request.POST.get("valid_code")
        if email:                             #如果email不为空
            user=LoginUser.objects.filter(email=email).first()  #调取数据库中LoginUser表中email=email的数据列传给user
            if user:                            #如果user存在（说明网页传来的数据和数据库对的上）
                db_password=user.password       #数据库中对应的密码值给变量db_password
                password=setPassword(password)  #把网页上加密的password赋值给新的password
                if db_password==password:       #如果都经过md5 加密的password值相等
                    response=HttpResponseRedirect("/Seller/index/")    #访问主页index
                    response.set_cookie("email",user.email)         #把数据库中的username下载到本地
                    response.set_cookie("user_id",user.id)         #把数据库中的id下载到本地缓存
                    request.session["email"]=user.email       #把用户信息放到服务器端
                    return response                            #返回请求
                else:
                    error_message="密码错误"
            else:
                error_message="用户名不存在"
        else:
            error_message="邮箱不可为空"
    return render(request,"seller/login.html",locals())

# 退出视图
def logout(request):
    response=HttpResponseRedirect("/login/")        #结果为返回到网页的登录界面
    keys=request.COOKIES.keys()                     #获取已登录的本地缓存的cookie值
    for key in keys:                                #遍历本地的cookie值
        response.delete_cookie(key)                 #结果中删除cookie
    del request.session["username"]                 #删除服务器端的用户信息
    return response

