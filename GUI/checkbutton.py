import tkinter 
from tkinter import ttk
win=tkinter.Tk()
name=tkinter.StringVar()
"""We are creating three check button widgets that differ in their states. The first is disabled
and has a check mark in it. The user cannot remove this check mark as the widget is
disabled.
The second check button is enabled, and by default, has no check mark in it, but the user
can click it to add a check mark.
The third check button is both enabled and checked by default. The users can uncheck and
recheck the widget as often as they like. """

win.title("GUI to enter the value")

a_label=ttk.Label(win,text="enter the value")
a_label.grid(column=0,row=0)

def click_me():
    action.configure(text="hello you entered the value "+number_choosen.get())
    

action=ttk.Button(win,text="Enter",command=click_me)
action.grid(column=2,row=0)



number_choosen=ttk.Combobox(win,width=12,textvariable=name)
number_choosen['values']=[1,2,3,4,5,6,7]
number_choosen.grid(column=1,row=0)

Chkvardis=tkinter.Tk()
check1=tkinter.Checkbutton(win,text="Disabled",variable=Chkvardis,state='disabled')
check1.select()
check1.grid(column=0,row=1,sticky=tkinter.W)

Chkvardun=tkinter.Tk()
check2=tkinter.Checkbutton(win,text="unchecked",variable=Chkvardun)
check2.deselect()
check2.grid(column=1,row=1,sticky=tkinter.W)

Chkvarden=tkinter.Tk()
check3=tkinter.Checkbutton(win,text="enable",variable=Chkvarden)
check3.select()
check3.grid(column=2,row=1,sticky=tkinter.W)

number_choosen.focus()

win.mainloop()
