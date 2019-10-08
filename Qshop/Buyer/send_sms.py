import requests

url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"

#APIID
account = "C70940786"
#APIkey
password = "4385fce9e0ba75e2af3290e6759e7287"

mobile = "15617830512"
content = "您的验证码是：5768843。请不要把验证码泄露给其他人。"
#定义请求的头部
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
#定义请求的数据
data = {
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}
#发起数据
response = requests.post(url,headers = headers,data=data)
    #url 请求的地址
    #headers 请求头部
    #data 请求的数据

print(response.content.decode())