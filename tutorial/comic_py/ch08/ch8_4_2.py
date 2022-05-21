# coding=utf-8
# 代码文件：ch08/ch8_4_2.py

def show_info(**info):
    print('-----show_info------')
    for key, value in info.items():
        print('{0} - {1}'.format(key, value))

show_info(name='Tony', age=18, sex=True)
show_info(sutdent_name='Tony', sutdent_no='1000')
