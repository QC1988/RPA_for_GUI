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
        wx.Frame.__init__(self,parent,id,title,pos = wx.DefaultPosition, size = wx.Size( 755,628 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        self.panel_inter1 = 0
        self.panel_inter2 = 0
        self.panel_inter3 = 0
        # self.panel_inter1_1 = 0

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        windowSizer = wx.BoxSizer(wx.HORIZONTAL)

        panelSideBarSizer = wx.BoxSizer(wx.VERTICAL)

        buttonSideBarSize = wx.BoxSizer(wx.VERTICAL)

        self.InitSideBar()
        buttonSideBarSize.Add(self.button_RMA, flag=wx.EXPAND)
        buttonSideBarSize.Add(self.button_NEP, flag=wx.EXPAND)
        buttonSideBarSize.Add(self.button_SBF, flag=wx.EXPAND)
        buttonSideBarSize.Add(self.button, flag=wx.EXPAND)


        self.setupStatusBar()
        self.InitInterPanel()
        self.InitLog()

        # panelSideBarSizer.Add(self._background, flag=wx.EXPAND

        self.panel_siderbar.SetSizer(buttonSideBarSize)
        self.panel_siderbar.Layout()
        buttonSideBarSize.Fit(self.panel_siderbar)

        panelSideBarSizer.Add(self.panel_siderbar,1, wx.EXPAND|wx.ALL, 5)

        windowSizer.Add(panelSideBarSizer,1, wx.EXPAND, 5)


        panelInterSizer = wx.BoxSizer(wx.VERTICAL)

        panelInterSizer.Add(self.panel_inter1, 1, wx.EXPAND| wx.ALL, 5)
        panelInterSizer.Add(self.panel, 1, wx.EXPAND| wx.ALL, 5)

        windowSizer.Add(panelInterSizer, 1, wx.EXPAND, 5)

        self.SetSizer(windowSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # wx.StaticBitmap(self.panel_siderbar,-1,wx.BitmapFromImage( self._background)) #显示图像


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


    #initialize Sidebar
    def InitSideBar(self):
        # self.panel_siderbar = wx.Panel(self, pos=(0, 0), size=(200, 800))  # 创建侧栏画板 
        self.panel_siderbar = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)  # 创建侧栏画板 
        self._background = wx.Image("background.jpg",type = wx.BITMAP_TYPE_ANY,)
        self._background = self._background.Rescale(200,150) #改变图像大小

        # panelSideBarSizer.Add(self._background, flag=wx.EXPAND)
 
        # self.button_RMA = wx.Button(self.panel_siderbar, label=u'RMA', pos=(0, 150), size=(200, 30))
        self.button_RMA = wx.Button(self.panel_siderbar, wx.ID_ANY, u"RMA", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_NEP = wx.Button(self.panel_siderbar, wx.ID_ANY, u"NEP", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_SBF = wx.Button(self.panel_siderbar, wx.ID_ANY, u"SBF", wx.DefaultPosition, wx.DefaultSize, 0)
        self.button = wx.Button(self.panel_siderbar,wx.ID_ANY, u"SBF", wx.DefaultPosition, wx.DefaultSize, 0)

        self.panel_siderbar.Bind(wx.EVT_BUTTON, self.Onclick_Ce, self.button_RMA)
        self.panel_siderbar.Bind(wx.EVT_BUTTON, self.Onclick_Ce, self.button_NEP)
        self.panel_siderbar.Bind(wx.EVT_BUTTON, self.Onclick_Ce, self.button_SBF)
        self.panel_siderbar.Bind(wx.EVT_BUTTON, self.clickbutton, self.button)

    # initial RMA
    def InitInterPanel(self):
        # self.panel_inter1 = wx.Panel(self, pos=(200, 0), size=(700, 200))
        self.panel_inter1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        wx.StaticText(self.panel_inter1,label="RMA list name",pos=(20,20))
        # wx.StaticText(self.panel_inter1, label="Password", pos=(20, 50))
        self.RMA_name=wx.TextCtrl(self.panel_inter1,pos=(120,15))
        # self._passwd = wx.TextCtrl(self.panel_inter1, pos=(110, 45),style=wx.TE_PASSWORD)

        self._submit_btn=wx.Button(self.panel_inter1,label=u'実行',pos=(100,100),size=(50,30))
        self.panel_inter1.Bind(wx.EVT_BUTTON,self.OnclickRMAbutton,self._submit_btn)

    def drawRMApanel(self):
        pass


    def drawNEPpanel(self):
        self.panel_inter2 = wx.Panel(self, pos=(200, 0), size=(700, 200))
        wx.StaticText(self.panel_inter2, label="NEP", pos=(130, 150))


    def drawSBFpanel(self):
        self.panel_inter3 = wx.Panel(self, pos=(200, 0), size=(700, 200))
        wx.StaticText(self.panel_inter3, label="SBF", pos=(130, 150))



    def InitLog(self):
        self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.label = new_std(self.panel, -1, "----末----", pos=(0, 0), size=(700, 400))
        sys.stdout = self.label
        sys.stderr = self.label

    def clickbutton(self, e):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # print("%Y-%m-%d %H:%M:%S"%time.localtime(time.time()))

	# def __del__(self):
    #     pass

    # def Onclick_Ce(self,event):
    #     event.Skip()

    # def OnclickRMAbutton(self, event):
    #     event.Skip()
