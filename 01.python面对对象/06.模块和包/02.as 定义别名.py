
#运行后暂停两秒打印hello


"""
1.导入time模块或者导入time模块的sleep功能

2.调用功能

3.打印hello


"""
#如果定义了别名就不能使用原来的模块名
# import time as tt
#
# tt.sleep(2)
# # time.sleep(2)
#
# print('hello')

#如果定义了别名就不能使用原来的功能名
from time import sleep as ting


ting(2)

print('hello')