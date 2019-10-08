
# import os
# lyid=os.getpid()
# print(lyid)
# xdd=os.cpu_count()
# print(xdd)

# 创建进程
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('子进程名和ID %s (%s)...' % (name, os.getpid()))
# if __name__=='__main__':
#     print('主进程的ID %s.' % os.getpid())
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
#     # p = Pool(3)
#     for i in range(10):
#         p.apply(down_load, args=(i,))
#     p.close()               #close()调用之后就不能继续添加新的进程了。
#     p.join()                #join()方法会等待所有子进程执行完毕
#     print('所有任务下载完毕.')



#获取进程pid
# from  multiprocessing import Pool
# import random
# import time,os
# def download(name):
#     print('下载任务: %s.' % os.getpid())
#     for i in range(1,4):
#         print('%s 下载了%s/3)' %(name,i))
#         time.sleep(random.random())
#     return name
# def alert(name):
#     print('%s下载完成' %name)
# list1 = ['天龙八部第%s部'%i for i in range(1,9)]
# if __name__ == '__main__':
#     print('当前进程:%s' % os.getpid())
#     pool = Pool(2)
#     for s in list1:
#         # pool.apply(func=download,args=(s,))
#         pool.apply_async(func=download,args=(s,),callback=alert)
#     pool.close()    # 阻塞主进程，让主进程等待所有子进程任务执行完毕之后才结束
#     pool.join()


