#encoding:utf-8



#1.定义类



class SweetPotato():
    def __init__(self):
        #被烤时间
        self.cook_time=0
        #被烤状态
        self.cook_state='生的'
        #调料列表
        self.condiments=[]


    def cook(self,time):
        #烤地瓜方法
        #先计算整体时间
        self.cook_time+=time
        #计算整体考地瓜的状态
        if 0<= self.cook_time <3:
            self.cook_state='生的'
        elif 3<= self.cook_time <5:
            self.cook_state='半生不熟'
        elif 5<= self.cook_time <8:
            self.cook_state='熟了'
        elif 8>= self.cook_time:
            self.cook_state='烤糊了'

    def add_condiments(self,condiments):
        self.condiments.append(condiments)
    def __str__(self):
        return f'这个地瓜的被烤过的时间是{self.cook_time},这个地瓜的状态是{self.cook_state},添加的调料有{self.condiments}'



#2.创建对对象并调用相应的类的实例方法


digua1=SweetPotato()
print(digua1)

digua1.cook(2)
digua1.add_condiments('辣椒面')
print(digua1)

digua1.cook(2)
print(digua1)

