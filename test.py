#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import tkinter as tk
# from tkinter.ttk import *
# from tkinter import ttk

# window = tk.Tk()
# boldStyle = ttk.Style ()
# boldStyle.configure("Bold.TButton", font = ('Georgia','12'))
# boldButton = ttk.Button(window, text = "Download", style = "Bold.TButton")
# boldButton.place(x=0,y=0)
# window.mainloop()

import tkinter as tk
from tkinter.ttk import *

class App():
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()

    master.title("Just my example")
    self.label = Label(frame, text="Type very long text:")

    self.entry = Entry(frame)

    self.button = Button(frame,
                         text="Quit", width=15,
                         command=frame.quit)


    self.slogan = Button(frame,
                         text="Hello", width=15,
                         command=self.write_slogan)

    self.label.grid(row=0, column=0)
    self.entry.grid(row=0, column=1)
    self.slogan.grid(row=1, column=0, sticky='e')
    self.button.grid(row=1, column=1, sticky='e')

  def write_slogan(self):
    print("Tkinter is easy to use!")

root = tk.Tk()
root.style = Style()
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
root.style.theme_use("default")

app = App(root)
root.mainloop()