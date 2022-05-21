# coding=utf-8
# 代码文件：ch10/ch10_2_3.py

i = input('请输入数字：')
n = 8888
try:
    result = n / int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n, i, result))
except (ZeroDivisionError, ValueError) as e:
    print("异常发生：{}".format(e))
