from tkinter import *
import tkinter.font as tkFont
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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
        self.value={ }
        
        
    def startapp(self):
        
        def senddata():
            if not firebase_admin._apps:
                cred = credentials.Certificate('path/to/serviceAccountKey.json') 
                firebase_admin.initialize_app(cred)
            
            db = firestore.client()
        
        
        
            #adding first data
            doc_ref = db.collection('patient').document('doc')
        
            doc_ref.set(self.val)
            
        
        def printdata(entrybox,entrybox1,canvas1):#Entrybox which takes the input area from the user
            text = entrybox.get()
            name=entrybox1.get()
            l=[]
            for x in text.split('/'):
                l.append(int(x))
            self.val={'systole':l[0],'diastole':l[1],'name':name}
            
        
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
        
        
        e1=Entry(self.obj)
        e2=Entry(self.obj)
        canvas1.create_window(200,100 , window=e1)
        canvas1.create_window(200,130 , window=e2)
        
        
        button = Button(self.obj,text='Enter',command=lambda:printdata(e1,e2,canvas1))
        canvas1.create_window(200, 150, window=button)
        
        button = Button(self.obj,text='senddata',command=lambda:senddata())
        canvas1.create_window(200, 180, window=button)
        
        
if __name__ == "__main__": 
    object1 = Tk()
    object2 = app(object1)
    object2.startapp()
    object1.mainloop()
