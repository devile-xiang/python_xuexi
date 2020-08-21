
#NameError
# print(num)


#ZeroDivisionError
# print(1/0)

#需求：尝试执行打印num,捕获异常类型nameerror,如果
# 捕获到这个异常类型，执行打印：有错误



try:
    # print(num)
    print(1/0)
except NameError:
    print('有错误')
except ZeroDivisionError:
    print('不能为0')


