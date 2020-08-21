import threading

import time
def task():
    time.sleep(1)
    #获取当前线程
    print(threading.current_thread())


if __name__ == '__main__':
    for i in range(20):
        sub_thread=threading.Thread(target=task)
        sub_thread.start()
        #线程之间是无序的，具体是由cpu来决定的