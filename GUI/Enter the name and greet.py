import tkinter 
from tkinter import ttk
win=tkinter.Tk()


win.title("vishal")
#win.resizable(False,False)
a_label=ttk.Label(win,text="enter the name")
a_label.grid(column=0,row=0)

def click_me():
    action.configure(text="hello"+name.get())
    

action=ttk.Button(win,text="click me!",command=click_me)
action.grid(column=0,row=2)


name=tkinter.StringVar()
name_entered=ttk.Entry(win,width=12,textvariable=name)
name_entered.grid(column=0,row=1)

win.mainloop()
