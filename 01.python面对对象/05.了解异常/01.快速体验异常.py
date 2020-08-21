

#需求：尝试打开text.txt（r）,如果文件不存在，只写方式打开w


"""
try:
    可能发生错误的代码
except:
    发生错误的时候执行的代码


"""


try:
    open('test.txt','r')
except:
    open('text.txt','w')
