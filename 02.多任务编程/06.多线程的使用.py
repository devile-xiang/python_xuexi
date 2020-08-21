#d导入线程模块

import threading
#创建子线程
import time
def sing():
    #获取当前线程
    current_thread=threading.current_thread()
    print("sing:",current_thread)
    for i in range(3):
        print("唱歌中...")
        time.sleep(0.2)


def dance():
    current_thread=threading.current_thread()
    print("dance:",current_thread)
    for i in range(3):
        print("跳舞中...")
        time.sleep(0.2)
#启动子线程


if __name__ == '__main__':
    current_thread=threading.current_thread()
    print("main:",current_thread)
    sing_thread=threading.Thread(target=sing)
    sing_thread.start()

    dance_thread=threading.Thread(target=dance())
    dance_thread.start()