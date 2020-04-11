import tkinter 
from tkinter import ttk
win=tkinter.Tk()
name=tkinter.StringVar()
'''GUI by adding drop-down combo boxes which can have
initial default values. While we can restrict the user to only certain choices, we can also
allow the user to type in whatever they wish.'''

win.title("GUI to enter the value")

a_label=ttk.Label(win,text="enter the value")
a_label.grid(column=0,row=0)

def click_me():
    action.configure(text="hello you entered the value "+number_choosen.get())
    

action=ttk.Button(win,text="Enter",command=click_me)
action.grid(column=0,row=2)



number_choosen=ttk.Combobox(win,width=12,textvariable=name)
number_choosen['values']=[1,2,3,4,5,6,7]
number_choosen.grid(column=0,row=1)

win.mainloop()
