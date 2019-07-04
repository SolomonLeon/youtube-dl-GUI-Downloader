#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from gui.connect import *
from gui.user import *
def settingwindow():
    settingconfig = readSetting()
    setting = tk.Toplevel()
    setting.geometry("370x83")
    setting.title("Setting")
    setting.resizable(False, False)
    def settingInit():
        b1.config(text=settingconfig["savedir"])
        e1.insert('end', settingconfig["proxy"])
    def choise():
        savedir = filedialog.askdirectory(parent=setting,initialdir=settingconfig["savedir"],title="Please select a folder:")
        settingconfig["savedir"]=savedir
        b1.config(text=settingconfig["savedir"])
    def Save():
        settingconfig["proxy"]=e1.get()
        if settingconfig["savedir"] != "":
            setSave(settingconfig)
    tk.Label(setting, text="Set directory to save file:").grid(row=0, sticky="w")
    tk.Label(setting, text="Set proxy:").grid(row=1, sticky="w")
    b1 = tk.Button(setting,text="Choise",command=choise,width=30)
    e1 = tk.Entry(setting,show=None,width=31)
    b1.grid(row=0, column=1, sticky="w")
    e1.grid(row=1, column=1, sticky="e")

    tk.Button(setting,text="Default",command=lambda:setSave(setDefault()),width=20).grid(row=2, column=0, sticky="e")
    tk.Button(setting,text="Save",command=Save,width=19).grid(row=2, column=1, sticky="e")

    settingInit()

def main():
    def checkDownload(url):
        if "www.youtube.com" not in url:
            tkinter.messagebox.showwarning(title='Warning: Please check your url', message='You must type in a Full youtube url!')
        else:
            startDownload(url)
    window = tk.Tk()
    window.title("Youtube-dl GUI")
    window.geometry("450x30")
    window.resizable(False, False)

    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Open file dir', command=openFiledir)
    filemenu.add_command(label='Setting', command=settingwindow)
    filemenu.add_command(label='Help', command=seeHelps)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)
    window.config(menu=menubar)

    urlbox = tk.Entry(window, show=None, font=("Arial",12))
    urlbox.place(x=0,y=0,width=350,height=30)
    tk.Button(window, text="download", font=('Arial', 12),command=lambda:checkDownload(url=urlbox.get())).place(x=350,y=0, width=100, height=30)

    window.mainloop()

if __name__ == "__main__":
    main()