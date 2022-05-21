# coding=utf-8
# 代码文件：ch13/ch13_7_3.py

import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="布局管理器嵌套", size=(300, 120))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,label="请单击按钮")
        b1 = wx.Button(parent=panel, id=10, label='Button1')
        b2 = wx.Button(parent=panel, id=11, label='Button2')

        # 创建水平方向的盒子布局管理器hbox对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # 添加b1到hbox布局管理
        hbox.Add(b1, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)
        # 添加b2到hbox布局管理
        hbox.Add(b2, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)

        # 创建垂直方向的盒子布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加静态文本到vbox布局管理器
        vbox.Add(self.statictext, proportion=1,
            flag=wx.CENTER|wx.FIXED_MINSIZE|wx.TOP, border=10)
        # 将水平hbox布局管理器对象到垂直vbox布局管理器对象
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)

        # 设置面板（panel）采用vbox布局管理器
        panel.SetSizer(vbox)

        # 将两按钮（b1和b2）的单击事件绑定到self.on_click方法
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Button1单击')
        else:
            self.statictext.SetLabelText('Button2单击')

app = wx.App()  # 创建应用程序对象

frm = MyFrame() # 创建窗口对象
frm.Show() # 显示窗口

app.MainLoop() # 进入主事件循环
