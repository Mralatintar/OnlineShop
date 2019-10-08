from django.test import TestCase
# for i in range(1,6):
#     c=f'x{i}'
# name='xx'
# print('my name is {}'.format(name))

import datetime,time
# print(time.time())
# code_time='2019-09-17 15:30:19.024935'
# now=time.mktime(datetime.datetime.now().timetuple())
# # db_time=time.mktime(code_time.timetuple())
# print(now)
import random
# string = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# valid_code = "".join([random.choice(string) for i in range(8)])
# print(valid_code)

#数字
# xdd=[]
# for i in range(10):
#     xdd.append(str(i))
# print(xdd)
# print("".join(xdd))
#字母
# xdd=[]
# for i in range(ord("A"),ord("z")):
#     xdd.append(str(chr(i)))
# xdd.pop()
# print(xdd)
# print("".join(xdd))
#----------------
#合并后
# def add_az():
#     num=[]
#     xdd=[]
#     ppd=[]
#     for n in range(0,10):
#         num.append(str(n))
#     for i in range(65,90):
#         xdd.append(chr(i))
#     for j in range(97,122):
#         ppd.append(chr(j))
#     xpp=num+xdd+ppd
#     jpp="".join(xpp)
#     valid_code = "".join([random.choice(jpp) for i in range(6)])
#     return valid_code

# xdd=[]
# for i in range(48,122):
#     xdd.append(str(chr(i)))

from django.test import TestCase
from Buyer.models import *
class Ourtest(TestCase):
    def setUp(self):
        pass
    def tear_insert(self):
        self.assertEquals("大菠萝1","大菠萝2")
    def tearDown(self):
        pass












# string='abcdefghijklmn'
# xdd="".join([random.choice(string) for k in range(4)])
# print(xdd)
# Create your tests here.
