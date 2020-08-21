#1.导入MangerSystem 模块



from ManagerSystem import *



#2.启动学员管理系统

#保证是当前文件运行才启动管理系统，if --创建对象并调用run方法
if __name__ == '__main__':
    student_mamager=StudentManager()
    student_mamager.run()