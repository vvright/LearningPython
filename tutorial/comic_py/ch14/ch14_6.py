# coding=utf-8
# 代码文件：ch14/ch14_6.py

import urllib.request
import json

url = 'http://localhost:8080/NoteWebService/note.do'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()

    py_dict = json.loads(json_data)
    # 返回所有的备忘录记录信息
    record_array = py_dict['Record']

    for record_obj in record_array:
        print('--------备忘录记录----------')
        print('备忘录ID：', record_obj['ID'])
        print('备忘录日期：', record_obj['CDate'])
        print('备忘录内容：', record_obj['Content'])
        print('用户ID：', record_obj['UserID'])
