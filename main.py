#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Used: https://github.com/arcticfox1919/tkinter-tabview/blob/master/dragwindow.py
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog, ttk
from gui.connect import *
from gui.user import *

class boot(tk.Tk):
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

def settingwindow():
    settingconfig = readSetting()
    setting = tk.Toplevel()
    setting.geometry("370x83")
    setting.title("Setting")
    setting.resizable(False, False)
    setting.wm_attributes("-toolwindow",True)
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
    def Paste():
        pass
    def checkDownload(url):
        if "www.youtube.com" not in url:
            tkinter.messagebox.showwarning(title='Warning: Please check your url', message='You must type in a Full youtube url!')
        else:
            startDownload(url)
    window = boot()
    window.title("Youtube-dl GUI")
    window.geometry("660x30")
    window.resizable(False, False)
    window.overrideredirect(True) 
    window.wm_attributes("-topmost",True)

    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Menu', menu=filemenu)
    filemenu.add_command(label='Open file dir', command=openFiledir)
    filemenu.add_command(label='Setting', command=settingwindow)
    filemenu.add_command(label='Help', command=seeHelps)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)
    window.config(menu=menubar)

    tk.Label(window, text="Youtube url:").place(x=0,y=0,width=80, height=30)
    urlbox = ttk.Entry(window, show=None, font=("Arial",10))
    urlbox.place(x=80,y=0,width=290,height=30)
    ttk.Button(window, text="Paste",command=Paste).place(x=370,y=0, width=50, height=30)
    tk.Label(window, text="Method:").place(x=420,y=0,width=55, height=30)
    choisework = ttk.Combobox(window,textvariable=tk.StringVar())
    choisework["values"] = ("Default Download","Choise size","Custom")
    choisework.current(0)
    choisework.place(x=475,y=0,width=125, height=30)
    ttk.Button(window, text="Go!",command=lambda:checkDownload(url=urlbox.get())).place(x=600,y=0, width=60, height=30)

    window.style = ttk.Style()
    window.style.theme_use("clam")#Georgia
    window.mainloop()
if __name__ == "__main__":
    main()