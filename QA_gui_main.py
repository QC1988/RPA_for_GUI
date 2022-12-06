#!/usr/bin/env python
# -*- coding: <utf-8> -*-

'''
QA_process_tool
'''
import wx
import QA_gui_logic


# class App(wx.App): # wx.App subclass
#     def __init__(self):
#     
#if rewrite __init__,it is necessary to call the __init__ in wx.App, otherwise the method would't be called.
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
