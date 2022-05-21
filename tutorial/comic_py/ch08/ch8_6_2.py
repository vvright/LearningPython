# coding=utf-8
# 代码文件：ch08/ch8_6_2.py

# 提供过滤条件函数
def f1(x):
    return x > 50 # 找出大于50元素

data1 = [66, 15, 91, 28, 98, 50, 7, 80, 99]
filtered = filter(f1, data1)
data2 = list(filtered)  # 转换为列表
print(data2)
