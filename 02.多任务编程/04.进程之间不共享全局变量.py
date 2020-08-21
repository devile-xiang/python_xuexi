import multiprocessing
import time
#定义全局变量：
g_list=list()
#添加数据的任务
def add_data():
    for i in range(3):
        #因为列表是可变类型，可以在原有内存的基础上修改数据，并且修改后内村地址不变
        #所以不需要加上global关键词
        #加上global 表示声明要修改全局变量的内存地址

        g_list.append(i)
        print("Add:",i)
        time.sleep(0.2)
    print("添加完成：",g_list)
    return g_list

#读取数据的任务
def read_data():
    print("read:",g_list)
#添加数据为子进程
#防止windows 系统创建子进程
#

if __name__ == '__main__':
    add_Process = multiprocessing.Process(target=add_data)

    add_Process.start()

    read_Process = multiprocessing.Process(target=read_data)
    #当前进程(主进程)等待添加数据完成后，执行这个进程
    add_Process.join()

    print("main:",g_list)
    read_Process.start()