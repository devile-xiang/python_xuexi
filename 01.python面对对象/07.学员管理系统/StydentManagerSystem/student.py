

#学生文件

class Student(object):
    def __init__(self,name,gender,tel):
        #姓名，性别，手机号

        self.name=name
        self.gender=gender
        self.tel=tel
    #添加__str__，方便查看数据，返回数据
    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'


# aa=Student('aa','nv',111)
#
#
# print(aa)












