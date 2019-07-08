#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon Zou
import os, subprocess
from gui.user import readSetting
from gui.window import selectWindow,customWindow,commandWindow
import tkinter.messagebox

def choiseDownload(url,method="Default Download"):#Split the download command
    if url == "":
        tkinter.messagebox.showwarning(title='Bad parameter', message="You must type a url.")
    elif method=="Default Download":
        commandWindow(command=getdownloadCommand(url=url,method="Default Download",sub=True))
    elif method=="Select Download":
        selectWindow(command=getdownloadCommand(url=url,method="Return Infor"),url=url)
    elif method=="Convert to mp3":
        commandWindow(command=getdownloadCommand(url=url,method="Custom",parameter="-x --audio-format mp3 --embed-thumbnail"))
    elif method=="Custom Download":
        customWindow(url=url)
    else:
        tkinter.messagebox.showwarning(title='Bad parameter', message="You did not choise the right method.")

def getdownloadCommand(url,method="Default Download",parameter=None,sub=None):#return command
    #accept: "Default Download","Return Infor","Custom"
    #I'm not sure if this program can work in all opera systems.Pleas try and tell me! :-P
    #If you want to help me, Please send me your codes as Pull Requests or issues.
    platform="windows"
    setting = {}
    setting = readSetting()
    savedir = "--output \""+setting["savedir"]+"%(title)s.%(ext)s"+"\""
    proxy = setting["proxy"]
    if sub == True:
        sub = "--write-sub --all-subs --sub-format \"ass/srt/best\" --convert-subs \"srt\" --embed-subs" #Experiments
    else:
        sub = ""
    if proxy != "":
        proxy ="--proxy \""+proxy+"\""

    if method == "Default Download":
        if platform == "windows":
            result = windowsDownload(parameter=None,proxy=proxy,savedir=savedir,url=url,sub=sub)
        return result

    elif method == "Return Infor":
        if platform == "windows":
            result = windowsDownload(parameter="-F",proxy=proxy,savedir=savedir,url=url,sub=sub)
        return result

    elif method == "Custom":
        if platform == "windows":
            result = windowsDownload(parameter=parameter,proxy=proxy,savedir=savedir,url=url,sub=sub)
        return result
    else:
        return "Bad parameter startdownload"

def windowsDownload(parameter,proxy,savedir,url,sub):
    if parameter == None:
        parameter = ""
    command = "youtube-dl "+parameter+" "+proxy+" "+savedir+" "+sub+" "+url
    # usecmd = "start cmd /c \""+command+" & pause\""
    # os.system(usecmd)
    return command