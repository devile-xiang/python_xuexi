import multiprocessing

import time



def task():
    while True:
    # for i in range(10):
        print("任务执行中...")
        time.sleep(0.2)

if __name__ == '__main__':
    sub_process=multiprocessing.Process(target=task)

    #把子进程设置为守护主进程，以后主进程退出子进程直接销毁
    # sub_process.daemon=True
    sub_process.start()

    #主进程盐城0.5秒钟
    time.sleep(0.5)
    #退出主进程之前，先让子进程进行销毁
    sub_process.terminate()
    print("over")
    #结论，主进程会等待子进程执行完成以后进程再退出
    #解决办法：主进程子进程销毁
    #1.让子进程设置成守护主进程，主进程退出子进程销毁，子进程会依赖主进程