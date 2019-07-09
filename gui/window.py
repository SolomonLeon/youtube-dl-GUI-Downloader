#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon Zou
import tkinter as tk
import tkinter.messagebox
import os,ast #, threading
from tkinter import filedialog
from gui.user import readSetting,setDefault,setSave

def settingWindow():
    settingconfig = readSetting()
    setting = tk.Toplevel()
    setting.geometry("370x83")
    setting.title("Settings")
    setting.resizable(False, False)
    # setting.wm_attributes("-toolwindow",True)
    setting.wm_attributes("-topmost",True)
    setting.wm_iconbitmap("icon.ico")

    def settingInit():
        b1.config(text=settingconfig["savedir"])
        e1.insert("end", settingconfig["proxy"])

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
    setting.mainloop()

def selectWindow(command,url):
    selectWindow = tk.Toplevel()
    selectWindow.geometry("400x300")
    selectWindow.title("Select size to dowanload.")
    selectWindow.wm_iconbitmap("icon.ico")

    def Submit():
        audiochoise = audioListbox.curselection()
        videochoise = videoListbox.curselection()
        if audiochoise and videochoise:
            audioid = audiodict[audioListbox.get(audiochoise)]
            videoid = videodict[videoListbox.get(videochoise)]
            parameter = "-f \""+videoid+"x"+audioid+"\""
            from gui.connect import getdownloadCommand
            commandWindow(command=getdownloadCommand(url=url,method="Custom",parameter=parameter,sub=True))
        else:
            tkinter.messagebox.showwarning(title="Error",message="You must select something to download.")

    tk.Label(selectWindow,text="Select \nvideo size:").place(x=0)
    tk.Label(selectWindow,text="Select \naudio size:").place(x=0,rely=0.5)

    videoListbox = tk.Listbox(selectWindow,exportselection=False)
    videoListbox.place(relwidth=1,x=80,rely=0,relheight=0.5,width=-180)
    yscrollbar1 = tk.Scrollbar(videoListbox,orient="vertical",command=videoListbox.yview)
    yscrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
    videoListbox.config(yscrollcommand=yscrollbar1.set)

    audioListbox = tk.Listbox(selectWindow,exportselection=False)
    audioListbox.place(relwidth=1,x=80,rely=0.5,relheight=0.5,width=-180)
    yscrollbar2 = tk.Scrollbar(audioListbox,orient="vertical",command=audioListbox.yview)
    yscrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
    audioListbox.config(yscrollcommand=yscrollbar2.set)

    tkinter.messagebox.showinfo(title='Ready to download informatiom', message="Be Patient!\nIf nothing is showed in this window for more than 3 mins, \nplease check your proxy setting and url.\nChick \"Sure\" to start downloading.")

    audiodict={}
    videodict={}
    for echo in os.popen(command):
        echo_list = echo.split()
        if "[youtube]" not in echo and "format" not in echo:
            if "audio" in echo:
                show = echo_list[-3]+" "+echo_list[-2]+" "+echo_list[-1]
                audiodict[show]=echo_list[0]
                audioListbox.insert('end', show)
            else:
                if "(best)"in echo:
                    show = echo_list[2]+" "+echo_list[3]+" "+echo_list[-4]+" "+echo_list[-2]
                else:
                    show = echo_list[2]+" "+echo_list[3]+" "+echo_list[-4]+" "+echo_list[-1]
                videodict[show]=echo_list[0]
                videoListbox.insert('end', show)

    tk.Button(selectWindow,text="Submit \nand \nDownload",command=Submit).place(relx=1,x=-85,rely=0.25,relheight=0.5)
    selectWindow.mainloop()

def customWindow(url):
    customWindow = tk.Toplevel()
    customWindow.geometry("520x250")
    customWindow.title("Custom Download")
    customWindow.wm_iconbitmap("icon.ico")
    commanddict={}

    def customConfig(do,dict):
        filetypes = [('Configfile', '.file')]
        if do =="save":
            file = filedialog.asksaveasfilename(parent=customWindow,initialdir=os.getcwd(),title="Please select a file name (*.file) for saving:",filetypes=filetypes)
            with open(file, "w")as f:
                f.write(str(dict))
        else:
            tkinter.messagebox.showinfo(title='Be careful!', message="Don't use those Configfile that other people send to you!")
            file = filedialog.askopenfilename(parent=customWindow,initialdir=os.getcwd(),title="Please select a file:",filetypes=filetypes)
            try:
                with open(file,"r") as f:
                    commanddictTemp = f.read()       
                    commanddictTemp = ast.literal_eval(commanddictTemp)
                commandlistbox.delete(0, "end")
                for key in commanddictTemp:
                    if commanddictTemp[key] == "":
                        line = key
                    else:
                        line = key+" \""+commanddictTemp[key]+"\""
                    commandlistbox.insert('end', line)
                    commanddict[key]=commanddictTemp[key]
            except:
                pass

    def getFullcommand():
        full = ""#add all parameter together
        for key in commanddict:
            if commanddict[key] == "":
                full = full+key+" "
            else :
                full = full+key+" \""+commanddict[key]+"\" "
        from gui.connect import getdownloadCommand
        full  = getdownloadCommand(url=url,method="Custom",parameter=full)#get full command
        return full

    def add():
        if option.get() != "":
            commandOption = option.get()
            commandParameter = parameter.get()
            if "-" not in commandOption:
                commandOption = "-"+commandOption
            commanddict[commandOption] = commandParameter
            if commandParameter == "":
                line = commandOption
            else:
                line = commandOption+" \""+commandParameter+"\""
            commandlistbox.insert('end', line)
        else:
            tkinter.messagebox.showwarning(title="Error",message="Option can't be empty.")

    def Select(*args):
        if commandlistbox.curselection():
            select = commandlistbox.get(commandlistbox.curselection())
            select = select.split(" ")[0]
            option.delete(0, "end")
            option.insert("end",select)
            try:
                parameter.delete(0,"end")
                parameter.insert("end",commanddict[select])
            except:
                pass

    def delete():
        if commandlistbox.curselection():
            try:
                select = commandlistbox.get(commandlistbox.curselection())
                select = select.split(" ")[0]
                commandlistbox.delete(commandlistbox.curselection())
                option.delete(0, "end")
                parameter.delete(0,"end")
                del commanddict[select]
            except:
                pass

    def showcommad():
        tkinter.messagebox.showinfo(title="Full command",message=getFullcommand())

    def help():
        tkinter.messagebox.showinfo(title="Help",message="You don't need to set \"--proxy\" or download dir;\n \"parameter\" can be empty but \"option\"must not be empty.")
    
    def startCustomdownload():
        commandWindow(getFullcommand())

    commandlistbox = tk.Listbox(customWindow,exportselection=False)
    commandlistbox.place(relwidth=1,x=0,y=0,relheight=1,heigh=-60)
    yscrollbar1 = tk.Scrollbar(commandlistbox,orient="vertical",command=commandlistbox.yview)
    yscrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
    commandlistbox.config(yscrollcommand=yscrollbar1.set)
    commandlistbox.bind("<<ListboxSelect>>",Select)

    tk.Label(customWindow,text="Option:").place(rely=1,x=0,y=-60,width=60,heigh=30)
    option = tk.Entry(customWindow)
    option.place(rely=1,x=60,y=-60,width=80,heigh=30)
    tk.Label(customWindow,text="Parameter:").place(rely=1,x=140,y=-60,width=70,heigh=30)
    parameter = tk.Entry(customWindow)
    parameter.place(rely=1,x=220,y=-60,relwidth=1,heigh=30,width=-330)
    tk.Button(customWindow,text="Add",command=add).place(rely=1,relx=1,x=-100,y=-60,heigh=30,width=50)
    tk.Button(customWindow,text="Del",command=delete).place(rely=1,relx=1,x=-50,y=-60,heigh=30,width=50)

    tk.Button(customWindow,text="?",command=help).place(rely=1,relx=1,x=-450,y=-30,heigh=30,width=30)
    tk.Button(customWindow,text="Save config",command=lambda:customConfig(do="save",dict=commanddict)).place(rely=1,relx=1,x=-410,y=-30,heigh=30,width=80)
    tk.Button(customWindow,text="Load config",command=lambda:customConfig(do="load",dict=None)).place(rely=1,relx=1,x=-330,y=-30,heigh=30,width=80)
    tk.Button(customWindow,text="Show full command",command=showcommad).place(rely=1,relx=1,x=-240,y=-30,heigh=30,width=130)
    tk.Button(customWindow,text="Download",command=startCustomdownload).place(rely=1,relx=1,x=-100,y=-30,heigh=30,width=100)

    customWindow.mainloop()

def commandWindow(command):#Failed in asynchronous fetch echo...I need help!!!
    usecmd = "start cmd /c \""+command+" & pause\""
    os.system(usecmd)
# def commandWindow(title,command):
#     if title=="" or command=="":
#         # tkinter.messagebox.showwarning(title='Bad parameter', message="You did not type a right command.")
#         title = "Network test"
#         command = "ping www.youtube.com"
#     commandWindow = tk.Toplevel()
#     commandWindow.geometry("400x300")
#     commandWindow.title(str(title))
#     commandWindow.wm_attributes("-toolwindow",True)
#     platform = "windows"
#     def ReTry():
#         if platform == "windows":
#             os.popen("taskkill /f /im cmd.exe")
#             commandBox.delete(0,'end')
#             runCommand(command=command)
#     def runCommand(command):
#         commandBox.insert('end', ">>>"+command)
#         def showEcho(command):
#             p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#             for line in iter(p.stdout.readline, b''):
#                 line = bytes.decode(line,"utf8","ignore")
#                 print(line)
#                 # commandBox.insert('end', line)
#         threading.Thread(target=showEcho, args=(command,))
#     commandBox = tk.Listbox(commandWindow)
#     commandBox.place(x=0,y=0,relwidth=1,relheight=1,width=-65)
#     tk.Button(commandWindow,text="ReTry",command=ReTry).place(heigh=30,width=60,relx=1,x=-60,y=0)
#     runCommand(command=command)