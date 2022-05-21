# coding=utf-8
# 代码文件：ch10/ch10_3.py

i = input('请输入数字：')
n = 8888
try:
    result = n / int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n, i, result))
except ZeroDivisionError as e:
    print("不能除以0，异常：{}".format(e))
except ValueError as e:
    print("输入的是无效数字，异常：{}".format(e))
finally:
    # 释放资源代码
    print('资源释放...')
