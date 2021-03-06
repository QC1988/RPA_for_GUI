#!/usr/bin/env python
# -*- coding: <utf-8> -*-

# from QA_gui_main import RMA_paras
import os
import wx
from sys import path
pwd = os.getcwd()
father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
path.insert(0, father_path)
path.insert(0, father_path+'\\Create_RMA_List')

import Create_RMA_list
import write_ini
import configparser
import QA_gui_template

class myconf(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=None)
    def optionxform(self, optionstr):
        return optionstr

class LogicFrame(QA_gui_template.Frame):

    #处理侧栏的点击事件
    def Onclick_Ce(self,event):
        # CeSizer = wx.BoxSizer(wx.VERTICAL)
        if event.GetEventObject() == self.button_RMA:
            print("RMA")
            # 如果需要显示的地方存在其他面板，删除
            if self.panel_inter2:
                #  self.panel_inter2.Destroy()
                 self.panel_inter2.Destroy()
            if self.panel_inter3:
                # self.panel_inter3.Destroy()
                self.panel_inter3.Destroy()
            if not self.panel_inter1 :
                self.InitInterPanel()
                
                # .Prepend(self.panel_inter1, wx.EXPAND| wx.ALL, 5)
                self.Layout()
                # self.panel_inter1 = wx.Panel(self, pos=(200, 0), size=(700, 200))
                # wx.StaticText(self.panel_inter1, label="RMA list name", pos=(20, 20))
                # self.RMA_name = wx.TextCtrl(self.panel_inter1, pos=(120,15))  
                # self.RMA_process_btn=wx.Button(self.panel_inter1,label=u'実行',pos=(100,100),size=(50,30))
                # self.panel_inter1.Bind(wx.EVT_BUTTON,self.OnclickRMAbutton,self.RMA_process_btn)
            #     if(denglu_flag == False):
            #         # self.InitButton()
            #         print("******")
            #     else:
            #         if not self.panel_inter1_1:
            #             self.panel_inter1_1 = wx.Panel(self, pos=(400, 150), size=(300, 300))
            #             wx.StaticText(self.panel_inter1_1, label="欢迎登陆", pos=(130, 150))

        if event.GetEventObject()==self.button_NEP:
            # 如果需要显示的地方存在其他面板，删除
            print("NEP")
            if self.panel_inter1:
                self.panel_inter1.Destroy()
            # if self.panel_inter1_1:
            #     self.panel_inter1_1.Destroy()
            if self.panel_inter3:
                self.panel_inter3.Destroy()
            if not self.panel_inter2 :
                self.drawNEPpanel()

        if event.GetEventObject() == self.button_SBF:
            print("SBF")
            if self.panel_inter1:
                self.panel_inter1.Destroy()
            # if self.panel_inter1_1:
            #     self.panel_inter1_1.Destroy()
            if  self.panel_inter2 :
                self.panel_inter2.Destroy()
            if not self.panel_inter3:
                self.drawSBFpanel()

    def GetRMAname(self):
        # print("GetRMAname")
        # print(self.RMA_name.GetValue())
        return self.RMA_name.GetValue()


    def OnclickRMAbutton(self, event):
        conf = myconf()
        if os.path.exists(father_path+'\\config.ini'):
            conf.read(father_path+'\\config.ini',encoding='utf-8')
            RMA_paras = conf['paras_for_RMA']
        else:
            print("The config file was not found!")
            exit()
        if event.GetEventObject()==self._submit_btn:
            RMA_paras['RMA_list_name'] = self.GetRMAname() + '.xlsx'
            config_path_tmp = father_path +'\\config.ini'
            print(config_path_tmp)
            write_ini.main(config_path_tmp, 'paras_for_RMA',RMA_paras)
            print(RMA_paras['RMA_list_name'])
            Create_RMA_list.main()


    # def buttonCebian1Click(self, event):
    #     # process for Events
    #     self.
