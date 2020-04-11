# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:52:59 2020

@author: Vishal
"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

win=tk.Tk()
menu_bar=Menu(win)


win.config(menu=menu_bar)
file_menu=Menu(menu_bar)


file_menu.add_command(label="New")
menu_bar.add_cascade(label="File",menu=file_menu)

scroll_w=30
scroll_h=3

scr=scrolledtext.ScrolledText(win,width=scroll_w,height=scroll_h,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)


win.mainloop()