# coding=utf-8
# 代码文件：ch08/ch8_8.py

data1 = [66, 15, 91, 28, 98, 50, 7, 80, 99]

filtered = filter(lambda x: (x > 50), data1)
data2 = list(filtered)
print(data2)

mapped  = map(lambda x: (x * 2), data1)
data3 = list(mapped) 
print(data3)
