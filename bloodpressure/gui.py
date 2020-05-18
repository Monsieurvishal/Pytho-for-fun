from tkinter import *
import tkinter.font as tkFont

class app():
    
    def __init__(self, obj):
        self.systole=0
        self.diastole=0
        self.obj=obj
        self.height = self.obj.winfo_screenheight() 
        self.width = self.obj.winfo_screenwidth()
        self.app_width = int(0.5*self.width)
        self.app_length = int(0.5*self.height)
        self.obj.geometry(str(self.app_width)+"x"+str(self.app_length))#Geometry is defined
        
        
        
    def startapp(self):
        
        def printdata(entrybox,canvas1):#Entrybox which takes the input area from the user
            text = entrybox.get()
            l=[]
            for x in text.split('/'):
                l.append(int(x))
                
            if l[0]<=120 and l[1]<=80:
                label1 = Label(self.obj, text='Normal')
                label1.config(font=('helvetica', 14))
                canvas1.create_window(200, 190, window=label1)
            elif (l[0]>120 and l[0]<129) and l[1]<80:
                label1 = Label(self.obj, text='Elevated')
                label1.config(font=('helvetica', 14))
                canvas1.create_window(200, 190, window=label1)
            elif (l[0]>=130 and l[0]<=139) or (l[1]>80 and l[1]<=89):
                label1 = Label(self.obj, text='Stage1 hypertension')
                label1.config(font=('helvetica', 14))
                canvas1.create_window(200, 190, window=label1)
            elif (l[0]>=140) or ( l[1]<90):
                label1 = Label(self.obj, text='Stage2 hypertension')
                label1.config(font=('helvetica', 14))
                canvas1.create_window(200, 190, window=label1)
            elif (l[0]>=180) or ( l[1]>=90):
                label1 = Label(self.obj, text='Call doctor Now')
                label1.config(font=('helvetica', 14))
                canvas1.create_window(200, 190, window=label1)
            else:
                label1 = Label(self.obj, text='Enter thevalid value')
                label1.config(font=('helvetica', 14))
                canvas1.create_window(200, 190, window=label1)
                
          
            
        canvas1 =Canvas(self.obj, width = 500, height = 500)
        canvas1.pack()
        
        
        label1 = Label(self.obj, text='Get blood pressure insights')
        label1.config(font=('helvetica', 14))
        canvas1.create_window(200, 25, window=label1)
        
        
        label2 = Label(self.obj, text='Enter systole and diastole rate\n eg: 120/80')
        label2.config(font=('helvetica', 14))
        canvas1.create_window(200, 70, window=label2)
        
        textin = StringVar()
        e=Entry(self.obj)
        canvas1.create_window(200,100 , window=e)
        
        
        button = Button(self.obj,text='Enter',command=lambda:printdata(e,canvas1))
        canvas1.create_window(200, 120, window=button)
         
