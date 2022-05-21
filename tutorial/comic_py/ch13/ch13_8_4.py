# coding=utf-8
# 代码文件：ch13/ch13_8_4.py

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='静态图片控件', size=(300, 300))
        self.panel = wx.Panel(parent=self)

        self.bmps = [wx.Bitmap('images/bird5.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('images/bird4.gif', wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('images/bird3.gif', wx.BITMAP_TYPE_GIF)]

        b1 = wx.Button(self.panel, id=1, label='Button1')
        b2 = wx.Button(self.panel, id=2, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1, id2=2)

        self.image = wx.StaticBitmap(self.panel, bitmap=self.bmps[0])

        # 创建垂直方向的布局管理器对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加标控件到布局管理器对象vbox
        vbox.Add(b1, proportion=1, flag=wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.EXPAND)
        vbox.Add(self.image, proportion=3, flag=wx.EXPAND)

        self.panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 1:
            self.image.SetBitmap(self.bmps[1])
        else:
            self.image.SetBitmap(self.bmps[2])
        self.panel.Layout()

app = wx.App()  # 创建应用程序对象
frm = MyFrame() # 创建窗口对象
frm.Show() # 显示窗口
app.MainLoop() # 进入主事件循环
