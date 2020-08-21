import time
import threading



g_list=[]
def add_data():
    for i in range(3):
        #每次循环异常把数据添加到全局变量
        g_list.append(i)
        print("add:",i)
        time.sleep(0.3)
    print("添加数据完成！！",g_list)
def read_data():
    print("read:",g_list)
if __name__ == '__main__':
    #创建添加数据的子线
    add_thread=threading.Thread(target=add_data)


    read_thread=threading.Thread(target=read_data)

    add_thread.start()
    add_thread.join()
    read_thread.start()
    #结论，线程之间共享全局变量