# coding=utf-8
# 代码文件：ch14/ch14_3_2.py

import urllib.request

url = 'http://localhost:8080/NoteWebService/note.do'

# 准备HTTP参数
params_dict = {'action': 'query', 'ID': '10'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)

# 字符串转换为字节序列对象
params_bytes = params_str.encode()  

req = urllib.request.Request(url, data=params_bytes)  # 发送POST请求
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)
