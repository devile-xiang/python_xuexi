import threading

import time
g_num=0
def task1():
    for i in range(1000000):
        #每循环一次给全局变量加1
        #表示声明一次给全局变量加1
        global g_num #表示要声明修改全局变量的内存地址
        g_num=g_num+1
    #代码执行到此，说明数据计算完成
    print("task1",g_num)
#循环100万次的任务
def task2():
    for i in range(1000000):
        #每循环一次给全局变量加1
        #表示声明一次给全局变量加1
        global g_num #表示要声明修改全局变量的内存地址
        g_num=g_num+1
    #代码执行到此，说明数据计算完成
    print("task2",g_num)
if __name__ == '__main__':
    #创建两个子线程
    first_thread=threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    first_thread.start()
    first_thread.join()#主线程等待第一个子线程执行完成以后代码再执行
    second_thread.start()