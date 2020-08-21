#encoding:utf-8





class Master(object):
    def __init__(self):
        self.kongfu='[古法煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Prentice(Master):
    # print("我们是徒弟")
    pass



daqiu=Prentice()

#显示
print(daqiu.kongfu)
daqiu.make_cake()