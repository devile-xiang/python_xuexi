

#如果一个模块文件中有__all__,只能调用__all__中的方法

from my_module2 import *


testA()


#testB,无法调用

#
testB()