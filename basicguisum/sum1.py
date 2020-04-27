import tkinter
from tkinter import *
from functools import partial

def sum(label,x1,x2):
    x1= (x1.get())
    x2= (x2.get())
    sum=int(x1)+int(x2)
    label.configure(text='sum is %d'%sum)
    return

win=Tk()

l1=Label(win,text="First number")
l1.grid(row=1,column=0)

l2=Label(win,text="First number")
l2.grid(row=2,column=0)

label=Label(win)
label.grid(row=3,column=0)

x1=StringVar()
x2=StringVar()

e1=Entry(win,textvariable=x1)
e1.grid(row=1,column=1)

e2=Entry(win,textvariable=x2)
e2.grid(row=2,column=1)

sum=partial(sum,label,x1,x2)
button=Button(win,text='Getsum',command=sum)
button.grid(row=3,column=3)

win.mainloop()
