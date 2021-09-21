#!/usr/bin/env python
# -*- coding: <utf-8> -*-
import wx
import time
import sys
# from wx.core import SYS_DEVICE_DEFAULT_FONT


class BlockWindow(wx.Panel):
    def __init__(self, parent, ID=-1, label="", pos=wx.DefaultPosition, size=(100, 25)):
        wx.Panel.__init__(self, parent, ID, pos, size, wx.RAISED_BORDER, label)
        self.label = label
        self.SetBackgroundColour("white")
        self.SetMinSize(size)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, evt):
        sz = self.GetClientSize()
        dc = wx.PaintDC(self)
        w,h = dc.GetTextExtent(self.label)
        dc.SetFont(self.GetFont())
        dc.DrawText(self.label, (sz.width-w)/2, (sz.height-h)/2)

class new_std(wx.TextCtrl):
    def __init__(self, parent, id, title, pos=(0, 0), size=(300, 100)):
        wx.TextCtrl.__init__(self, parent, id, title, pos, size, style=wx.TE_MULTILINE)
        self.old_stdout=sys.stdout
        self.old_stderr=sys.stderr

    def write(self, output):
        output=output.replace('\n', '\r\n')
        self.WriteText(output)

    def back_to_console(self):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

class Frame(wx.Frame): #2 wx.Frame子类
    def __init__(self,parent = None,id = -1,title ='QA processing tool'):
        wx.Frame.__init__(self,parent,id,title,size=(960,760))
        self.panel_Celan1 = None
        self.panel_Celan2 = None
        self.panel_Celan3 = None
        self.panel_Celan1_1 = None

        self.setupStatusBar()
        self.InitCelan()
        self.InitButton()
        self.InitLog()

    def clickbutton(self, e):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # print("%Y-%m-%d %H:%M:%S"%time.localtime(time.time()))

    #initialize Statebar
    def setupStatusBar(self):
        # Statebar
        sb = self.CreateStatusBar(2)  # 2代表将状态栏分为两个
        self.SetStatusWidths([-1, -2])  # 比例为1：2
        self.SetStatusText("Ready", 0)  # 0代表第一个栏，Ready为内容
        # timmer
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.Notify()

    # Real-time display of time
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d %H:%M:%S', t)
        self.SetStatusText(st, 1)  # 这里的1代表将时间放入状态栏的第二部分上

    # # 初始化登陆
    # def InitButton(self):
    #     self.panel_Celan1 = wx.Panel(self, pos=(400, 150), size=(300, 300))
    #     wx.StaticText(self.panel_Celan1,label="Username",pos=(20,20))
    #     wx.StaticText(self.panel_Celan1, label="Password", pos=(20, 50))
    #     self._username=wx.TextCtrl(self.panel_Celan1,pos=(110,15))
    #     self._passwd = wx.TextCtrl(self.panel_Celan1, pos=(110, 45),style=wx.TE_PASSWORD)

    #     self._submit_btn=wx.Button(self.panel_Celan1,label=u'提交',pos=(100,100),size=(50,30))
    #     self.panel_Celan1.Bind(wx.EVT_BUTTON,self.Onclick,self._submit_btn)

    # #处理登陆事件
    # def Onclick(self,event):
    #     global denglu_flag
    #     if event.GetEventObject()==self._submit_btn:
    #         user = self.GetUsername()
    #         passwd = self.GetPasswd()
    #         print(user+":"+passwd)
    #         if(user == "wenli"and passwd == "123456"):
    #             denglu_flag=True
    #             self.panel_Celan1.Destroy()
    #             self.panel_Celan1_1 =wx.Panel(self, pos=(400, 150), size=(300, 300))
    #             wx.StaticText(self.panel_Celan1_1, label="欢迎登陆", pos=(130, 150))
    # def GetUsername(self):
    #     return self._username.GetValue()

    # def GetPasswd(self):
    #     return self._passwd.GetValue()

    # initial RMA
    def InitButton(self):
        self.panel_Celan1 = wx.Panel(self, pos=(200, 0), size=(700, 200))
        wx.StaticText(self.panel_Celan1,label="RMA list name",pos=(20,20))
        # wx.StaticText(self.panel_Celan1, label="Password", pos=(20, 50))
        self.RMA_name=wx.TextCtrl(self.panel_Celan1,pos=(120,15))
        # self._passwd = wx.TextCtrl(self.panel_Celan1, pos=(110, 45),style=wx.TE_PASSWORD)

        self._submit_btn=wx.Button(self.panel_Celan1,label=u'実行',pos=(100,100),size=(50,30))
        self.panel_Celan1.Bind(wx.EVT_BUTTON,self.OnclickRMAbutton,self._submit_btn)

    #initialize Sidebar
    def InitCelan(self):
        self.panel_Celan = wx.Panel(self, pos=(0, 0), size=(200, 800))  # 创建侧栏画板 
        CelanSizer = wx.BoxSizer(wx.VERTICAL)

        self._background = wx.Image("background.jpg",type = wx.BITMAP_TYPE_ANY,)
        self._background = self._background.Rescale(200,150) #改变图像大小

        # CelanSizer.Add(self._background, flag=wx.EXPAND)
        wx.StaticBitmap(self.panel_Celan,-1,wx.BitmapFromImage( self._background)) #显示图像
        # self._caidan1 = wx.Button(self.panel_Celan, label=u'RMA', pos=(0, 150), size=(200, 30))
        self._caidan1 = wx.Button(self.panel_Celan, label=u'RMA', pos=(0, 150), size=(200, 30))
        self._caidan2 = wx.Button(self.panel_Celan, label=u'NEP', pos=(0, 180), size=(200, 30))
        self._caidan3 = wx.Button(self.panel_Celan, label=u'SBF', pos=(0, 210), size=(200, 30))
        self.button = wx.Button(self.panel_Celan, label=u"Button", pos=(0, 240), size=(200, 30))
        
        CelanSizer.Add(self._caidan1, flag=wx.EXPAND)
        CelanSizer.Add(self._caidan2, flag=wx.EXPAND)
        CelanSizer.Add(self._caidan3, flag=wx.EXPAND)
        CelanSizer.Add(self.button, flag=wx.EXPAND)

        self.panel_Celan.Bind(wx.EVT_BUTTON, self.Onclick_Ce, self._caidan1)
        self.panel_Celan.Bind(wx.EVT_BUTTON, self.Onclick_Ce, self._caidan2)
        self.panel_Celan.Bind(wx.EVT_BUTTON, self.Onclick_Ce, self._caidan3)
        self.panel_Celan.Bind(wx.EVT_BUTTON, self.clickbutton, self.button)

    def InitLog(self):
        self.panel = wx.Panel(self, pos=(200, 200), size=(700, 400))
        self.label = new_std(self.panel, -1, "----末----", pos=(0, 0), size=(700, 400))
        sys.stdout = self.label
        sys.stderr = self.label

	# def __del__(self):
    #     pass

    def Onclick_Ce(self,event):
        event.Skip()

    def OnclickRMAbutton(self, event):
        event.Skip()
