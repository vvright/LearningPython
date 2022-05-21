# coding=utf-8
# 代码文件：ch13/ch13_6.py

import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="事件处理", size=(300, 180))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,label="请单击OK按钮", pos=(110, 20))
        b = wx.Button(parent=panel, label='OK', pos=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

    def on_click(self, event):
        self.statictext.SetLabelText('Hello, World.')

app = wx.App()  # 创建应用程序对象

frm = MyFrame() # 创建窗口对象
frm.Show() # 显示窗口

app.MainLoop() # 进入主事件循环
