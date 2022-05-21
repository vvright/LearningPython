# coding=utf-8
# 代码文件：ch13/ch13_5.py

import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="第一个wxPython程序!", size=(400, 300), pos=(100, 100))
        panel = wx.Panel(parent=self)
        statictext = wx.StaticText(parent=panel, label='Hello World!', pos=(10, 10))

app = wx.App()  # 创建应用程序对象

frm = MyFrame() # 创建窗口对象
frm.Show() # 显示窗口

app.MainLoop() # 进入主事件循环
