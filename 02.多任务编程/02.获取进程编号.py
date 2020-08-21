#1.导入进程包
import multiprocessing
import time

import os
#跳舞任务：
def dance():
    for i in range(3):
        # 获取当前进程的编号
        print("当前的进程编号：%s"%os.getpid())
        #获取当前进程的名字
        print("dance:",multiprocessing.current_process())

        #获取父进程编号：
        print("父进程编号：", os.getppid())
        print("跳舞中...")
        time.sleep(0.2)
#唱歌任务
def song():
    for i in range(3):
        #获取当前进程的编号
        print("当前的进程编号：%s" % os.getpid())
        # 获取当前进程的名字
        print("dance:", multiprocessing.current_process())
        # 获取父进程编号：
        print("父进程编号：", os.getppid())
        print("唱歌中...")
        time.sleep(0.2)

#2.创建子进程(自己手动创建的进程为子进程，在__init__.py文件中已经导入的process类)

#group:进程组


#启动相应的进程




if __name__ == '__main__':
    # 获取父进程编号：
    print("***********父进程编号：", os.getppid())

    dance_pricess = multiprocessing.Process(target=dance, args="",name="dance_pricess")
    print("dance_pricess:",dance_pricess)
    dance_pricess.start()

    song_pricess = multiprocessing.Process(target=song, args="",name="song_pricess")
    print("song_pricess:",song_pricess)
    song_pricess.start()



