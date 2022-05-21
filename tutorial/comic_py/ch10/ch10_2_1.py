# coding=utf-8
# 代码文件：ch10/ch10_2_1.py

i = input('请输入数字：')
n = 8888
try:
    result = n / int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n, i, result))
except ZeroDivisionError as e:  # except:
    print("不能除以0，异常：{}".format(e))
