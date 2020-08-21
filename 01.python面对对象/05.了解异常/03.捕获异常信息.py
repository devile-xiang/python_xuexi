#捕获异常信息


try:
    print(num)

except (NameError,ZeroDivisionError) as result:
    print(result)