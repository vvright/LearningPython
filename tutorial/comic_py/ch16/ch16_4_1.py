# coding=utf-8
# 代码文件：ch16/ch16_4_1.py

import threading
import time

# 共享变量
value = []

# 线程体函数
def thread_body():
    # 当前线程对象
    print('t1子线程开始...')
    for n in range(2):
        print('t1子线程执行...')
        value.append(n)
        # 线程休眠
        time.sleep(2)
    print('t1子线程结束。')

# 主线程
print('主线程开始执行...')
# 创建线程对象t1
t1 = threading.Thread(target=thread_body)
# 启动线程t1
t1.start()
# 主线程被阻塞，等待t1线程结束
t1.join()
print('value = {0}'.format(value))
print('主线程继续执行...')
