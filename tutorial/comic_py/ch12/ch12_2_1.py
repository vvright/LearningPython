# coding=utf-8
# 代码文件：ch12/ch12_2_1.py

# 使用finally关闭文件
f_name = 'test.txt'
f = None
try:
    f = open(f_name)
    print('打开文件成功')
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print('文件不存在，请先使用ch12_1.py程序创建文件')
except OSError as e:
    print('处理OSError异常')
finally:
    if f is not None:
        f.close()
        print('关闭文件成功')
