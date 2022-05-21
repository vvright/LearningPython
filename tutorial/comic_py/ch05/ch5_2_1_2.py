# coding=utf-8
# 代码文件：ch5/ch5_2_1_2.py

i = 0

while i * i < 10:
    i += 1
    if i == 3:
        break
    print(str(i) + ' * ' + str(i) + ' =', i * i)
else:
    print('While Over!')
