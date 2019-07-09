#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon Zou
# https://api.github.com/repos/ytdl-org/youtube-dl/releases/latest
from urllib.request import urlopen
import json, re, os

os.system("title Youtube-dl installer")
os.system("color 02")
try:
    os.system("del youtube-dl.exe")
except e:
    pass
os.system("cls")

print("[*]Getting info from github")
u = urlopen("https://api.github.com/repos/ytdl-org/youtube-dl/releases/latest")
resp = json.loads(u.read().decode('utf-8'))
allassets = resp["assets"]
for key in allassets:
    if re.match(".+youtube-dl\\.exe$",key["browser_download_url"]):
        url = key["browser_download_url"]
        path = str(os.getcwd()).replace("/", os.path.sep)+os.path.sep
        os.system("cls&color f0")
        print("[*]Notes: After download, please move \"youtube-dl.exe\" into \n[*]"+path)
        os.system("pause")
        os.system("cls")
        print("[!]I highly recommend you to download FFmpeg because some features of youtube-dl depend on FFmpeg")
        print("[!]I will open the download page of FFmpeg at the same time. Please move the \"ffmpeg.exe\" into \n[!]"+path)
        os.system("pause")
        os.system("explorer "+url)
        os.system("explorer https://ffmpeg.zeranoe.com/builds/")
        os.system("pause")
        break