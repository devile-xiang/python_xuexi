#四锁，一直等待对象释放锁的情景叫做死锁
import threading
import time

#声明锁
lock=threading.Lock()


#需求：多线程同事根据下表在列表中取值，要保证同一时刻只能有一个线程去取值
def get_value(index):
    lock.acquire()
    my_list=[1,4,6]
    if index >=len(my_list):
        print("下表越界")
         #取值不成功，也需要释放互斥锁，不要影响后面的线程取值
        #锁需要在合适的地方释放
        lock.release()
        return
    value=my_list[index]
    print(value)
    lock.release()


if __name__ == '__main__':
    #创建大量线程，同事执行根据下表取值的任务
    for i in range(10):
        sub_thread=threading.Thread(target=get_value,args=(i,))
        #启动线程执行任务
        sub_thread.start()
