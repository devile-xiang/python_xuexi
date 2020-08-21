#定义类

class A(object):
    a=0
    def __init__(self):
        self.b=1

#创建对象

aa=A()

#返回这个所有类的所有字典
print(A.__dict__)
#返回我们定义的字典
print(aa.__dict__)