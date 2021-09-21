#!/usr/bin/env python
# -*- coding: <utf-8> -*-

'''
QA_process_tool
'''
import wx
import QA_gui_logic

# class App(wx.App): #5 wx.App子类
#     def __init__(self):
#     #如果要重写__init__,必须调用wx.App的__init__,否则OnInit方法不会被调用
#         wx.App.__init__(self)
#     def OnInit(self):
#         self.frame=QA_gui_template.Frame()
#         self.SetTopWindow(self.frame)
#         self.frame.Show()
#         return True


if __name__=="__main__":
    # global RMA_paras
    app = wx.App()
    frame = QA_gui_logic.LogicFrame(None)
    frame.Show()
    global denglu_flag
    denglu_flag = False
    app.MainLoop()
