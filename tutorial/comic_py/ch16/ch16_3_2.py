# coding=utf-8
# 代码文件：ch16/ch16_3_2.py

import threading
import time

class SmallThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)
    # 线程体函数
    def run(self):
        # 当前线程对象
        t = threading.current_thread()
        for n in range(5):
            # 当前线程名
            print('第{0}次执行线程{1}'.format(n, t.name))
            # 线程休眠
            time.sleep(2)
        print('线程{0}执行完成！'.format(t.name))

# 主线程
# 创建线程对象t1
t1 = SmallThread()
# 创建线程对象t2
t2 = SmallThread(name='MyThread')
# 启动线程t1
t1.start()
# 启动线程t2
t2.start()
