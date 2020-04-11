"""Using scrolled text widgets"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win=tk.Tk()

scroll_w=30
scroll_h=3

scr=scrolledtext.ScrolledText(win,width=scroll_w,height=scroll_h,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)

win.mainloop()
