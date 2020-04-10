
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:14:09 2020

@author: Vishal
"""

import tkinter 
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("mygui")

        self.label = tkinter.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = tkinter.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = tkinter.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("congrats vishal!")

root = tkinter.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
