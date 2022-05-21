# coding=utf-8
# 代码文件：ch13/ch13_3.py

import wx

# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = wx.Frame(None, title="第一个wxPython程序!", size=(400, 300), pos=(100, 100))
# 显示窗口
frm.Show()

# 进入主事件循环
app.MainLoop()
