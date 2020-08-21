

#继承L子类默认继承父类的所有数学和方法



# 1.定义父类

class A(object):
    def __init__(self):
        self.num=1
    def info_print(self):
        print(self.num)


# 2.定义自雷 继承父类

class B(A):
    pass
# 创建对象，验证结论


class C(B):

    pass


result=B()
result.info_print()


result1=C()


print(result1.info_print())