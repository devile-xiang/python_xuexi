#1.导入进程包
import multiprocessing
import time
#跳舞任务：
def dance():
    for i in range(3):
        print("跳舞中...")
        time.sleep(0.2)
#唱歌任务
def song():
    for i in range(3):
        print("唱歌中...")
        time.sleep(0.2)

#2.创建子进程(自己手动创建的进程为子进程，在__init__.py文件中已经导入的process类)

#group:进程组


#启动相应的进程




if __name__ == '__main__':
    dance_pricess = multiprocessing.Process(target=dance, args="")

    dance_pricess.start()

    song_pricess = multiprocessing.Process(target=song, args="")

    song_pricess.start()



