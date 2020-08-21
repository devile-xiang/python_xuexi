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
xiaoqiu.make_master_cake()
xiaoqiu.make_shcool_cake()