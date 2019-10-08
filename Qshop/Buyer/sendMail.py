import smtplib
from email.mime.text import MIMEText

subject="快乐讯息"                              #发送的标题
content="""                                    
hai，我是小新，很荣幸给你发邮箱。 
"""                                             #发送的内容

sender="18239907498@163.com"                    #发送者邮箱
recver="""                                      
    827582114@qq.com,
    1004797744@qq.com,
    1196635726@qq.com
"""                                             #接受者邮箱
password="wojiushidi1ren"                       #密码
message=MIMEText(content,"plain","utf-8")       #内容，编码方式

message["Subject"]=subject                      #实例化
message["From"]=sender
message["TO"]=recver

smtp=smtplib.SMTP_SSL("smtp.163.com",465)       #发送端口
smtp.login(sender,password)                         #登录
smtp.sendmail(sender,recver.split(",\n"),message.as_string())   #邮箱的字符串变列表
smtp.close()                                            #关闭邮箱