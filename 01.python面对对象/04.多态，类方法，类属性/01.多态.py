#需求：警务人员和警犬一起工作，警犬分两种：追击敌人和追查毒品，携带不同的警犬



#定义父类，提供公用方法：警犬和 人


class Dog(object):
    def work(self):
        pass


#2.定义自雷，子类重写父类方法：定义2个累表示不同的警犬


class ArmyDog(Dog):
    def work(self):
        print('追击敌人...')

class DrugDog(Dog):
    def work(self):
        print('追击毒品...')
class Person(object):
    def work_with_dog(self,dog):
        dog.work()


#创建对象，调用不同的功能，传入不同的对象，观察执行的结果

AD=ArmyDog()
DD=DrugDog()

daqiu=Person()


daqiu.work_with_dog(AD)

daqiu.work_with_dog(DD)
