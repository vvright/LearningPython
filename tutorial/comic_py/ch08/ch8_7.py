# coding=utf-8
# 代码文件：ch08/ch8_7.py

def calc(opr):
    if opr == '+':
        return lambda a, b: (a + b)  # 替代add函数
    else:
        return lambda a, b: (a - b)  # 替代sub函数

f1 = calc('+')
f2 = calc('-')
print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
