# coding=utf-8
# 代码文件：ch14/ch14_5.py

import urllib.request

url = 'http://localhost:8080/NoteWebService/logo.png'

req = urllib.request.Request(url)
with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = 'download.png'
    with open(f_name, 'wb') as f:
        f.write(data)
        print('下载文件成功')
