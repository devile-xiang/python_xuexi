import threading
import time



def show_info(name,age):
    print("name:%s，age:%d"%(name,age))



if __name__ == '__main__':
    #用元组传参，元组传输的顺序要和接受的顺序保持一致
    sub_thread=threading.Thread(target=show_info,args=("李四",20))
    sub_thread.start()
    #以字典方式方式传参，字典名字要和接受名字保持一致
    sub_thread1 = threading.Thread(target=show_info, kwargs={"name":"张三","age":25})
    sub_thread1.start()
