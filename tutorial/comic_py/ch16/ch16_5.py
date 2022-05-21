# coding=utf-8
# 代码文件：ch16/ch16_5.py

import threading
import time
import urllib.request

# 线程停止变量
isrunning = True

# 工作线程体函数
def workthread_body():
    while isrunning:
        # 线程开始工作
        print('工作线程执行下载任务...')
        download()
        # 线程休眠
        time.sleep(5)
    print('工作线程结束。')

# 控制线程体函数
def controlthread_body():
    global isrunning
    while isrunning:
        # 从键盘输入停止指令exit
        command = input('请输入停止指令：')
        if command == 'exit':
            isrunning = False
            print('控制线程结束。')

def download():
    url = 'http://localhost:8080/NoteWebService/logo.png'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        data = response.read()
        f_name = 'download.png'
        with open(f_name, 'wb') as f:
            f.write(data)
            print('下载文件成功')

# 主线程
# 创建工作线程对象workthread
workthread = threading.Thread(target=workthread_body)
# 启动线程workthread
workthread.start()

# 创建控制线程对象controlthread
controlthread = threading.Thread(target=controlthread_body)
# 启动线程controlthread
controlthread.start()
