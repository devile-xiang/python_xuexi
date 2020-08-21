import multiprocessing

import time
def task():
    time.sleep(1)
    #获取当前进程
    print(multiprocessing.current_process())


if __name__ == '__main__':
    for i in range(20):
        sub_thread=multiprocessing.Process(target=task)
        sub_thread.start()

        #进程之间执行也是无序的，操作系统调度进程来决定