# coding=utf-8
# 代码文件：ch13/ch13_4.py

import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="第一个wxPython程序!", size=(400, 300), pos=(100, 100))
        # 你的代码


# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = MyFrame()
# 显示窗口
frm.Show()

# 进入主事件循环
app.MainLoop()
