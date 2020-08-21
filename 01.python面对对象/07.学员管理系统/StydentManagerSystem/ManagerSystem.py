#管理系统文件

from student import Student

class StudentManager(object):
    def __init__(self):
        #存储学员数据----列表
        self.student_list=[]

    #一.程序入口函数，启动程序后执行的函数

    def run(self):
        #1.加载数据
        self.load_student()

        while True:
            #2.显示共功能菜单
            self.show_menu()

            #3.用户输入功能序号
            menu_num=int(input('请输入您需要的功能序号：'))
            #4.根据用户输入的序号执行不同的功能
            if menu_num==1:
                #添加学员
                self.add_student()
            elif menu_num==2:
                #删除学院
                self.del_student()

            elif menu_num==3:
                #修改学院信息
                self.modify_student()
            elif menu_num==4:
                #查询学员信息
                self.search_student()
            elif menu_num==5:
                #显示所有学员信息
                self.show_student()
            elif menu_num==6:
                #保存学员信息
                self.seve_student()
            elif menu_num==7:
                #退出系统
                break

    #二.系统功能函数
    # 2.1显示功能  -- 打印学号的功能对应关系  --静态
    @staticmethod
    def show_menu():
        print('请选择如下功能：')

        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')


    # 2.2添加学员
    def add_student(self):
        #1.用户输入姓名。性别。手机号
        name=input('请输入您的姓名：')
        gender=input('请输入您的性别：')
        tel = input('请输入您的手机号：')
        #2.创建学员对象-- 类？类在student 文件里 先导入student模块，在创建对象
        student=Student(name,gender,tel)

        #3.将对象添加到对象列表
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    # 2.3删除学员

    def del_student(self):
        #用户输入目标学员的姓名
        del_name=input('请输入你要删除的学员姓名：')
        #遍历学员列表，如果用户输入的学员存在则删除学员对象，否则提示学员不存在
        for i in  self.student_list:
            if del_name ==i.name:
                #删除该学员对象
                self.student_list.remove(i)
                break
        else:
            #循环正常结束执行的代码。循环结束都没有删除任何一个对象，所以说明用户输入的目标用户不存在
            print('查无此人')
        print(self.student_list)

    # 2.4修改学员信息
    def modify_student(self):
        #1.用户输入目标学员的姓名
        modify_name=input('请输入要修改的学员的姓名：')
        #2.编列列表数据，如果学员存在修改姓名性别手机号，否则提示学员不存在
        for i in self.student_list:
            if modify_name ==i.name:
                i.name=input('姓名：')
                i.gender=input('性别：')
                i.tel=input('手机号：')
                print(f'修改学员信息成功，姓名{i.name},姓名{i.gender},手机号{i.tel}')
                break
        else:
            print('查无此人')
        print('修改学员信息')
    # 2.5查询学员信息
    def search_student(self):
        #1.用户输入目标学员姓名

        student_name=input('请输入你要查询学员的姓名：')


        for i in self.student_list:
            if i.name==student_name:
                print(f'你查询的学员姓名是{i.name},性别是：{i.gender},电话号码是：{i.tel}')
                break
        else:
            print('查无此人！！！')


        print('查询学员信息')
    # 2.6显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t手机号 ')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel} ')


    # 2.7保存学员信息
    def seve_student(self):
        #1.打开文件

        f=open('student.data', 'w')
        #注意1：文件写入的数据不能是对象的内存地址，需要把对象数据转换成列表字典数据在存储

        new_lsit=[i.__dict__ for i in self.student_list]

        #文件写入字符串数据
        f.write(str(new_lsit))

        #关闭文件
        f.close()


        print('保存学员信息')

    # 2.8加载学员信息

    def load_student(self):
        try:
            #尝试r,打开文件，如果有异常就W
            f=open('student.data', 'r')

        except:
            #异常w打开文件
            f = open('student.data', 'w')
        else:
            #读取文件
            data=f.read()
            #2.文件读取的数据都是字符串且字符串内部为字典数据，故需要转换数据类型再
            #转换字典为对象后存储到学员列表
            new_lsit=eval(data)
            #使用列表推导式，遍历使用实例，然后传入学生信息列表
            self.student_list=[Student(i['name'],i['gender'],i['tel']) for i in new_lsit]
        finally:
            #关闭文件
            f.close()
