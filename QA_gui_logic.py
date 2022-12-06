#!/usr/bin/env python
# -*- coding: <utf-8> -*-

# from QA_gui_main import RMA_paras
import os
import wx
import time
from sys import path

from wx.core import Sleep
pwd = os.getcwd()
father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
path.insert(0, father_path)
path.insert(0, father_path+'\\Create_RMA_List')

import Create_RMA_list
import configparser
import QA_gui_template

class myconf(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=None)
    def optionxform(self, optionstr):
        return optionstr

class LogicFrame(QA_gui_template.Frame):

    # handle the click event of the sidebar
    def Onclick_Ce(self,event):
        # CeSizer = wx.BoxSizer(wx.VERTICAL)
        if event.GetEventObject() == self.button_RMA:
            print("RMA button was pressed.")
            # if there is some other panel exsit in the display area then delete it
            if self.panel_inter1:
                print("RMA panel now.")
                pass

            else:
                if self.panel_inter2:
                    self.panel_inter2.Destroy()
                    print("destory inter1")
                if self.panel_inter3:
                    self.panel_inter3.Destroy()
                    print("destory inter1")
                self.drawRMApanel()
                print("Changed to RMA panel.")
                

            # if self.panel_inter2:
            #     #  self.panel_inter2.Destroy()
            #      self.panel_inter2.Destroy()
            #      self.drawRMApanel()
            #      print("panel_inter2")
            # if self.panel_inter3:
            #     # self.panel_inter3.Destroy()
            #     self.panel_inter3.Destroy()
            #     self.drawRMApanel()
            #     print("panel_inter3")
            # if not self.panel_inter1 :
            #     print("panel_inter1")
            #     # LogicFrame.Destory()
            #     # self.InitInterPanel()
            #     self.drawRMApanel()
                
            #     # .Prepend(self.panel_inter1, wx.EXPAND| wx.ALL, 5)
            #     self.Layout()
            #     # self.panel_inter1 = wx.Panel(self, pos=(200, 0), size=(700, 200))
            #     # wx.StaticText(self.panel_inter1, label="RMA list name", pos=(20, 20))
            #     # self.RMA_name = wx.TextCtrl(self.panel_inter1, pos=(120,15))  
            #     # self.RMA_process_btn=wx.Button(self.panel_inter1,label=u'process',pos=(100,100),size=(50,30))
            #     # self.panel_inter1.Bind(wx.EVT_BUTTON,self.OnclickRMAbutton,self.RMA_process_btn)
            # #     if(denglu_flag == False):
            # #         # self.InitButton()
            # #         print("******")
            # #     else:
            # #         if not self.panel_inter1_1:
            # #             self.panel_inter1_1 = wx.Panel(self, pos=(400, 150), size=(300, 300))
            # #             wx.StaticText(self.panel_inter1_1, label="Welcome.", pos=(130, 150))

        if event.GetEventObject()==self.button_NEP:
            # if there is some other panel exsit in the display area then delete it
            print("NEP was pressed.")
            if self.panel_inter2:

                print("NEP panel now.")
                pass

            else :
                if self.panel_inter1:
                    self.panel_inter1.Destroy()
                    print("destory inter1")
                if self.panel_inter3:
                    self.panel_inter3.Destroy()
                    print("destory inter3")                    
                self.drawNEPpanel()
                print("Change to RMA panel.")
                

        if event.GetEventObject() == self.button_SBF:
            print("SBF")
            if self.panel_inter1:
                self.panel_inter1.Destroy()
            # if self.panel_inter1_1:
            #     self.panel_inter1_1.Destroy()
            if  self.panel_inter2 :
                self.panel_inter2.Destroy()
            if not self.panel_inter3:
                print("SBF button was pressed.")
                self.drawSBFpanel()

    def GetRMAname(self):
        # print("GetRMAname")
        # print(self.RMA_name.GetValue())
        return self.RMA_name.GetValue()


    def OnclickRMAbutton(self, event):
        conf = myconf()
        if os.path.exists(father_path+'\\config.ini'):
            # conf.read(father_path+'\\config.ini',encoding='utf-8')
            # RMA_paras = conf['paras_for_RMA']
            pass
        else:
            print("The config file was not found!")
            exit()
        if event.GetEventObject()==self._submit_btn:
            # RMA_paras['RMA_list_name'] = self.GetRMAname() + '.xlsx'
            RMA_paras_RMA_list_name = self.GetRMAname() + '.xlsx'
            config_path_tmp = father_path + '\\config.ini'
            print(config_path_tmp)
            # write_ini.main(config_path_tmp, 'paras_for_RMA', RMA_paras)
            # print(RMA_paras['RMA_list_name'])
            print(RMA_paras_RMA_list_name)
            # time.sleep(3)
            Create_RMA_list.main(RMA_paras_RMA_list_name)


    # def buttonCebian1Click(self, event):
    #     # process for Events
    #     self.
