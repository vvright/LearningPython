# coding=utf-8
# 代码文件：ch06/ch6_6.py

s_dict = {102: '张三', 105: '李四', 109: '王五'}

print('---遍历键---')
for s_id in s_dict.keys():
    print('学号：' + str(s_id))

print('---遍历值---')
for s_name in s_dict.values():
    print('学生：' + s_name)

print('---遍历键:值---')
for s_id, s_name in s_dict.items():
    print('学号：{0} - 学生：{1}'.format(s_id, s_name))
