import wx

'''
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='demo',
                         pos=(100,100),size=(500,300))  # 创建窗口
        frame.Show()    #显示窗口
        return True

if __name__ == '__main__':
    app = App()     #创建App类的实例
    app.MainLoop()  #调用主循环

'''


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title='demo'):
        wx.Frame.__init__(self, parent, id, title,
                          pos=(-1,-1), size=(420, 350))
        panel = wx.Panel(self)  # 创建画板

        # 创建标题
        title = wx.StaticText(panel, label='登陆', pos=(180, 20))  # 创建标题
        font = wx.Font(20, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)  # 字体样式
        title.SetFont(font)  # 设置字体

        # 创建文本
        self.label_user = wx.StaticText(panel, label='用户名:', pos=(50, 80))
        self.text_user = wx.TextCtrl(panel, pos=(100, 80), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label='密  码:', pos=(50, 120))
        self.text_pwd = wx.TextCtrl(panel, pos=(100, 120), size=(235, 25), style=wx.TE_PASSWORD)

        #创建按钮
        self.btn_confirm = wx.Button(panel,label='确定',pos=(105,170))
        self.btn_cancel=wx.Button(panel,label='取消',pos=(210,170))

        #绑定事件
        self.btn_confirm.Bind(wx.EVT_BUTTON,self.submit)
        #self.btn_cancel.Bind(wx.EVT_BUTTON,self.cancel)

    def submit(self,event):
        wx.MessageBox('login')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, -1)
    frame.Show()
    app.MainLoop()
