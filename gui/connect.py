#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from gui.user import readSetting
def startDownload(url,method="download"):
    setting = {}
    setting = readSetting()
    savedir = "--output \""+setting["savedir"]+"%(title)s.%(ext)s"+"\""
    proxy = setting["proxy"]
    if method == "download":
        if proxy != "":
            proxy ="--proxy \""+proxy+"\""
        command = ".\\exefiles\\youtube-dl.exe "+proxy+" "+savedir+" "+url
        usecmd = "start cmd /c \""+command+" & pause\""
        os.system(usecmd)