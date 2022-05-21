# coding=utf-8
# 代码文件：ch08/ch8_4_1.py

def sum(*numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

print(sum(100.0, 20.0, 30.0))  # 输出150.0
print(sum(30.0, 80.0))  # 输出110.0
