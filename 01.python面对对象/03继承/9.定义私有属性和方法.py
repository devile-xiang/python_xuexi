#encoding:utf-8




class Master(object):
    def __init__(self):
        self.kongfu='[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu='[黑马煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')



class Prentice(School,Master):
    def __init__(self):

        self.kongfu='[独创煎饼果子技术]'
        #私有变量
        self.__money=200000
    #定义私有方法，私有属性和私有方法都是前面加__,
    # 私有属性和方法 不能被继承给子类

    def __info_print(self):
        print('这是私有方法！！！')
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


class Tusun(Prentice):
    pass




xiaoqiu=Tusun()
#徒孙默认继承父类的所有方法
xiaoqiu.make_cake()
#继承引用私有变量报错
# print(xiaoqiu.__money)
xiaoqiu.make_master_cake()
xiaoqiu.make_shcool_cake()
#继承私有方法报错
# xiaoqiu.__info_print()