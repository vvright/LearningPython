# coding=utf-8
# 代码文件：ch12/ch12_6.py

f_name = 'logo.png'

with open(f_name, 'rb') as f:
    b = f.read()
    copy_f_name = 'logo2.png'
    with open(copy_f_name, 'wb') as copy_f:
        copy_f.write(b)
        print('文件复制成功')
