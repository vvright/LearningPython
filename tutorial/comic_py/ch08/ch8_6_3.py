# coding=utf-8
# 代码文件：ch08/ch8_6_3.py

# 提供变换规则的函数
def f1(x):
    return x * 2 # 变换规则乘以2

data1 = [66, 15, 91, 28, 98, 50, 7, 80, 99]
mapped  = map(f1, data1)
data2 = list(mapped )  # 转换为列表
print(data2)
