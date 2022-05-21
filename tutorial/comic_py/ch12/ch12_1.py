# coding=utf-8
# 代码文件：ch12/ch12_1.py

f = open('test.txt', 'w+')
f.write('World')
print('①创建test.txt文件，World写入文件')

f = open('test.txt', 'r+')
f.write('Hello')
print('②打开test.txt文件，Hello覆盖文件内容')

f = open('test.txt', 'a')
f.write(' ')
print(r'③打开test.txt文件，在文件尾部追加空格" "')

# fname = r'C:\Users\tony\OneDrive\漫画Python\code\ch12\test.txt'
# fname = 'C:\\Users\\tony\\OneDrive\\漫画Python\\code\\ch12\\test.txt'
fname = 'C:/Users/tony/OneDrive/漫画Python/code/ch12/test.txt'
f = open(fname, 'a+')
f.write('World')
print('④打开test.txt文件，在文件尾部追加World')
