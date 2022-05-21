# coding=utf-8
# 代码文件：ch14/ch14_4_2.py

import urllib.request
import json

url = 'http://localhost:8080/NoteWebService/note.do?action=query&ID=10'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print('JSON字符串：',json_data)

    py_dict = json.loads(json_data)
    print('备忘录ID：', py_dict['ID'])
    print('备忘录日期：', py_dict['CDate'])
    print('备忘录内容：', py_dict['Content'])
    print('用户ID：', py_dict['UserID'])
