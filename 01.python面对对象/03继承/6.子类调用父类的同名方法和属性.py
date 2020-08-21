#encoding:utf-8




class Master(object):
    def __init__(self):
        self.kongfu='[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(Master):
    def __init__(self):
        self.kongfu='[黑马煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')



class Prentice(School):
    def __init__(self):

        self.kongfu='[独创煎饼果子技术]'
    def make_cake(self):
        #不加自己的初始化，kongfu属性值是上一次执行的kongfu属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master_cake(self):
        #初始化师傅的kongfu
        Master.__init__(self)
        Master.make_cake(self)
    def make_shcool_cake(self):
        # 初始化学校的kongfu
        School.__init__(self)
        School.make_cake(self)







daqiu=Prentice()


print(daqiu.kongfu)
daqiu.make_cake()
daqiu.make_master_cake()
daqiu.make_shcool_cake()
daqiu.make_cake()



#结论如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法的时候，调用的是子类的同名属性和方法