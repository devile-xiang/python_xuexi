import multiprocessing

#显示信息的任务

def show_info(name,age):
    print(name,age)


#创建子进程
if __name__ == '__main__':
    #以元祖方式传参，元祖里面的元素顺序要和函数的参数顺序保持一致
    # sub_process = multiprocessing.Process(target=show_info, args=("李四", 20))
    #
    # sub_process.start()
    #字典穿值，只需要对应名字就行
    # sub_process=multiprocessing.Process(target=show_info,kwargs={"age":"20","name":"风气"})
    # sub_process.start()

    sub_process=multiprocessing.Process(target=show_info,args=("风起",),kwargs={"age":"20"})
    sub_process.start()

