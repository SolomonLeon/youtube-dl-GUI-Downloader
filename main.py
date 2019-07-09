#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon Zou
#If you want to help me, Please send me your codes or ideas by Pull Requests or issues.
#I won't add Auto updatater into Beta version. Please  :-P
import tkinter as tk
import pyperclip
from tkinter import filedialog, ttk
from gui.connect import choiseDownload
from gui.user import *
from gui.window import *

class boot(tk.Tk):# from: https://github.com/arcticfox1919/tkinter-tabview/blob/master/dragwindow.py
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self,master=None):
        tk.Tk.__init__(self,master) 
        self.bind('<B1-Motion>', self._on_move)
        self.bind('<ButtonPress-1>', self._on_tap)

    def _on_move(self, event):
        offset_x = event.x_root - self.root_x
        offset_y = event.y_root - self.root_y
        if self.width and self.height:
            geo_str = "%sx%s+%s+%s" % (self.width, self.height,
                                       self.abs_x + offset_x, self.abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (self.abs_x + offset_x, self.abs_y + offset_y)
        self.geometry(geo_str)

    def _on_tap(self, event):
        self.root_x, self.root_y = event.x_root, event.y_root
        self.abs_x, self.abs_y = self.winfo_x(), self.winfo_y()

def main():
    def Paste():
        urlbox.delete(0, 'end')
        urlbox.insert("end",str(pyperclip.paste()))
    window = boot()
    window.title("Youtube-dl GUI downloader")
    window.geometry("660x30")
    window.resizable(False, False)
    window.overrideredirect(True) 
    window.wm_attributes("-topmost",True)
    # window.wm_iconbitmap("icon.ico")
    # window.wm_attributes("-alpha", 0.7)

    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Menu', menu=filemenu)
    filemenu.add_command(label='Open file dir', command=openFiledir)
    filemenu.add_command(label='Setting', command=settingWindow)
    filemenu.add_command(label='Help', command=seeHelps)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)#Something strange happend with "window.quit"...I don't know why...
    window.config(menu=menubar)

    tk.Label(window, text="Video url:  ").place(x=0,y=0,width=80, height=30)
    urlbox = ttk.Entry(window, show=None, font=("Arial",10))
    urlbox.place(x=80,y=0,width=290,height=30)
    ttk.Button(window, text="Paste",command=Paste).place(x=370,y=0, width=50, height=30)
    tk.Label(window, text="Method:").place(x=420,y=0,width=55, height=30)
    choisemethod = ttk.Combobox(window,textvariable=tk.StringVar())
    choisemethod["values"] = ("Default Download","Select Download","Convert to mp3","Custom Download")
    choisemethod.current(0)
    choisemethod.place(x=475,y=0,width=125, height=30)
    ttk.Button(window, text="Go!",command=lambda:choiseDownload(url=urlbox.get(), method=choisemethod.get())).place(x=600,y=0, width=60, height=30)

    window.style = ttk.Style()
    window.style.theme_use("clam")
    window.mainloop()
if __name__ == "__main__":
    main()