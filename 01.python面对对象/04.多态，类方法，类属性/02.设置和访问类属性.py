#定义类，定义属性

class Dog(object):
    #类属性的优点：记录的某项数据 始终保持一致，则定义类属性。

    # 实例属性要求每个对象为其单独开辟一份内存空间来记录数据，二类属性

    tooch=10



#2.创建对象

wangcai=Dog()

xiaohei=Dog

#3.访问类属性：类和对象


print(Dog.tooch)


xiaohei.tooch=20

print(wangcai.tooch)

print(xiaohei.tooch)