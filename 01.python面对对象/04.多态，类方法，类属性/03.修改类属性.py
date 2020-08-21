

class Dog(object):
    tooch=10


wangcai=Dog()
xiaohei=Dog()


# 1.类修改
#
# Dog.tooch=20
# print(Dog.tooch)
# print(wangcai.tooch)
# print(xiaohei.tooch)



# 2类属性只能通过类修改不能通过实例属性修改！！


wangcai.tooch=300
print(Dog.tooch)

print(wangcai.tooch)
print(xiaohei.tooch)
