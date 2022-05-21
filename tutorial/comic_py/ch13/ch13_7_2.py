# coding=utf-8
# 代码文件：ch13/ch13_7_2.py

import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="事件处理", size=(300, 180))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,label="请单击OK按钮")
        b = wx.Button(parent=panel, label='OK')
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

        # 创建垂直方向的盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加静态文本到vbox布局管理器
        vbox.Add(self.statictext, proportion=1, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP, border=30)
        # 添加按钮b到vbox布局管理器
        vbox.Add(b, proportion=1, flag=wx.EXPAND|wx.BOTTOM, border=10)
        # 设置面板（panel）采用vbox布局管理器
        panel.SetSizer(vbox)

    def on_click(self, event):
        self.statictext.SetLabelText('Hello, World.')

app = wx.App()  # 创建应用程序对象
frm = MyFrame() # 创建窗口对象
frm.Show() # 显示窗口
app.MainLoop() # 进入主事件循环
