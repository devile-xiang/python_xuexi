
# 1.定义类，私有类属性，类方法获取这个私有类属性

class Dog(object):


    __tooth=10


    @classmethod

    def get_tooth(cls):
        return cls.__tooth

#2.创建对象,调用类方法

wangcai=Dog()


print(wangcai.get_tooth())