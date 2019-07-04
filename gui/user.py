#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, ast
def openFiledir():
    os.system("explorer \""+readSetting()["savedir"]+"\"")

def readSetting():
    try:
        with open("setting.file","r") as f:
            setting = f.read()       
            setting = ast.literal_eval(setting)
    except Exception:
        setSave(setDefault())
        setting = setDefault()
    return setting

def setDefault():
    dict={}
    dict["savedir"]=str(os.getcwd()).replace("/", os.path.sep)#兼容各种系统，实验
    dict["proxy"]=""
    return dict
def setSave(dict):
    dict["savedir"] = dict["savedir"].replace("/", os.path.sep) + os.path.sep
    with open("setting.file", "w") as f:
        f.write(str(dict))
def seeHelps():
    try:
        os.system("start help.bat")
    except Exception as e:
        os.system("start cmd /c \"@echo off&title Help&echo Please go to Github for help\"")