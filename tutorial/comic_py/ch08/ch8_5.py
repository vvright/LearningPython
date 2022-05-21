# coding=utf-8
# 代码文件：ch08/ch8_5.py

# 创建全局变量x
x = 20

def print_value():
    global x  # 将x变量提升为全局变量
    x = 10
    print("函数中x = {0}".format(x))


print_value()
print("全局变量x = {0}".format(x))
