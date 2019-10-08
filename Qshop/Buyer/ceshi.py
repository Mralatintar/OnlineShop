# from Seller.models import *

# xdd=Goods.objects.all()
# print(xdd)

# goods_type=GoodsType.objects.all()
# print(goods_type)

# class Xdd():
#     def xuu(self):
#         ooi=[1,2,3,4,5,6.7,8]
#         return ooi
# iee=Xdd()
# print(iee)
# c=iee.xuu()
# print(c)
# import sys
# print(sys.version_info)
# print(sys.version)
# print("hello,world")
# print('goodbye, world', end='!\n')
# print('hello', 'world', sep=', ', end='!')
# import this
import turtle
import time

# import turtle as t
# t.setpos(0,-150) #移到坐标0，-150
# t.pendown() #放下笔开始绘
# t.pencolor('violet') #设笔颜色
# for i in range(0,24):
#     t.forward(100)
#     t.left(105)
#     t.stamp()
# while True:
#     f = float(input('请输入华氏温度: '))
#     c = (f - 32) / 1.8
#     print('%.1f华氏度 = %.1f摄氏度' % (f, c))


# import math
#
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

# while True:
#     year = int(input('请输入年份: '))
#     # 如果代码太长写成一行不便于阅读 可以使用\或()折行
#     is_leap = (year % 4 == 0 and year % 100 != 0 or
#                year % 400 == 0)
#     print(is_leap)




# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
#
# turtle.mainloop()

# from random import *
# xdd=[]
# for i in range(1,6):
#     xdd.append(i)
#
#
# face = randint(1, 6)
# if face == 1:
#     result = '唱首歌'
# elif face == 2:
#     result = '跳个舞'
# elif face == 3:
#     result = '学狗叫'
# elif face == 4:
#     result = '做俯卧撑'
# elif face == 5:
#     result = '念绕口令'
# else:
#     result = '讲冷笑话'
# print(result)

# salary = float(input('本月收入: '))
# insurance = float(input('五险一金: '))
# diff = salary - insurance - 3500
# if diff <= 0:
#     rate = 0
#     deduction = 0
# elif diff < 1500:
#     rate = 0.03
#     deduction = 0
# elif diff < 4500:
#     rate = 0.1
#     deduction = 105
# elif diff < 9000:
#     rate = 0.2
#     deduction = 555
# elif diff < 35000:
#     rate = 0.25
#     deduction = 1005
# elif diff < 55000:
#     rate = 0.3
#     deduction = 2755
# elif diff < 80000:
#     rate = 0.35
#     deduction = 5505
# else:
#     rate = 0.45
#     deduction = 13505
# tax = abs(diff * rate - deduction)
# print('个人所得税: ￥%.2f元' % tax)
# print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))

# 打印99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

from math import sqrt
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break

# row = int(input('请输入行数: '))
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

# for x in range(1, 20):
#     for y in range(1, 33):
#         z = 100 - y - x
#         if z % 3 == 0 and 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡：', x, '只', '母鸡：', y, '只', '小鸡：', z, '只')

# from multiprocessing import Pool
# import time
# def down_load(movie_name):
#     for i in range(5):
#         print('电影:{},下载进度{}%'.format(movie_name, (i / 4 * 100)))
#         time.sleep(1)
#     return movie_name
# def alert(movie_name):
#     print('恭喜{}下载完成了...'.format(movie_name))
# if __name__ == '__main__':
#     movie_lst = ['魔兽世界', '权利的游戏', '西部世界','碟中谍','战狼','红海行动','唐伯虎点秋香']
#     pool = Pool(6)
#     for movie_name in movie_lst:
#         # 创建异步任务，放入进程池中
#         pool.apply_async(down_load, (movie_name,),
#                          callback=alert)
#     pool.close()
#     pool.join()



# import os
# lyid=os.getpid()
# print(lyid)


# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('子进程名和ID %s (%s)...' % (name, os.getpid()))
# if __name__=='__main__':
#     print('父进程的ID %s.' % os.getpid())       #获取
#     p = Process(target=run_proc, args=('记事本',))  #创建一个Process实例,传参name='记事本'
#     print('子进程开始.')
#     p.start()
#     p.join()                #join()方法可以等待子进程结束后再继续往下运行。
#     print('子进程结束.')

#进程池，异步任务
# from multiprocessing import Pool
# import os, time, random
# def down_load(i):
#     print('任务 %s (%s)...' % (i, os.getpid()))
#     # time.sleep(random.random() * 3)
#     time.sleep(1)
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(3)
#     for i in range(10):
#         p.apply_async(down_load, args=(i,))
#     print('等待子进程完成...')
#     p.close()               #close()调用之后就不能继续添加新的进程了。
#     p.join()                #join()方法会让主进程等待所有子进程执行完毕（阻塞主进程）
#     print('所有任务下载完毕.')


#进程池，异步任务同步任务
# from multiprocessing import Pool
# import os, time, random
# def down_load(i):
#     print('任务 %s (%s)...' % (i, os.getpid()))
#     # time.sleep(random.random() * 3)
#     time.sleep(1)
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(3)
#     for i in range(10):
#         p.apply(down_load, args=(i,))
#     print('等待子进程完成...')
#     p.close()               #close()调用之后就不能继续添加新的进程了。
#     p.join()                #join()方法会等待所有子进程执行完毕
#     print('所有任务下载完毕.')



#获取进程pid
from  multiprocessing import Pool
import random
import time,os
def download(name):
    print('下载任务: %s.' % os.getpid())
    print(os.getpid())
    for i in range(1,4):
        print('%s 下载了%s/3)' %(name,i))
        time.sleep(random.random())
    return name
def alert(name):
    print('%s下载完成' %name)
list1 = ['天龙八部第%s部'%i for i in range(1,9)]
if __name__ == '__main__':
    print('当前进程:%s' % os.getpid())
    pool = Pool(2)
    for s in list1:
        # pool.apply(func=download,args=(s,))
        pool.apply_async(func=download,args=(s,),callback=alert)
    pool.close()    # 阻塞主进程，让主进程等待所有子进程任务执行完毕之后才结束
    pool.join()






