# coding=utf-8
# 代码文件：ch12/ch12_2_2.py

# 使用with as自动资源管理
f_name = 'test.txt'
with open(f_name) as f:
    content = f.read()
    print(content)
