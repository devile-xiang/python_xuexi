#方法一


"""
1.导入

import 包名.模块名

2.调用功能

包名.模块名。功能（）

"""


#导入mypackage包下的模块1.使用这个模块内的info_print1函数


#这种方式是可以使用的
from mypackage import my_module2


#方法二：再使用 from mypackage import * 的时候
#注意：必须在包的__init__.py文件中添加__all__=[]，控制允许导入的模块列表
from mypackage import *
from mypackage import *


my_module2.info_print()
my_module1.info_print()





