from tkinter import *
import tkinter.font as tkFont
import random as r


class app():
    
    def __init__(self, obj):
        self.obj = obj
        self.obj.title("User Interface")
        self.height = self.obj.winfo_screenheight() 
        self.width = self.obj.winfo_screenwidth()
        self.app_width = int(0.5*self.width)
        self.app_length = int(0.5*self.height)
        self.obj.geometry(str(self.app_width)+"x"+str(self.app_length))
        self.ycount=0
        self.ccount=0
        self.draw=0
        self.pwin=0
        self.ploose=0
        self.pdraw=0
        self.total=0
        
        
    def letsplay(self):
        def quit(game):
            game.destroy()
            
            
        def logic1(entrybox,game):
                self.total=self.total+1

                computer_choice = r.choice(["P", "R", "S"])
                text = entrybox.get()
                if 'R' in text:
                    label1 = Label(game, text= "you Entered "+str(text) )
                    label1.after(2000 , lambda: label1.destroy())
                    label1.pack()
                elif "P" in text:
                    label2 = Label(game, text= "you Entered "+str(text) )
                    label2.after(2000 , lambda: label2.destroy())
                    label2.pack()            
                elif "S" in text:
                    label3 = Label(game, text= "you Entered "+str(text) )
                    label3.after(2000 , lambda: label3.destroy())
                    label3.pack()
                else:
                    label4 = Label(game, text= "you Entered "+str(text) )
                    label4.after(2000 , lambda: label4.destroy())
                    label4.pack()           


                if "R" in computer_choice:
                    label5 = Label(game, text= "computer Entered "+str(computer_choice) )
                    label5.after(2000 , lambda: label5.destroy())
                    label5.pack()
                elif "P" in computer_choice:
                    label6 = Label(game, text= "computer Entered "+str(computer_choice) )
                    label6.after(2000 , lambda: label6.destroy())
                    label6.pack()
                else:
                    label7 = Label(game, text= "computer Entered "+str(computer_choice) )
                    label7.after(2000 , lambda: label7.destroy())
                    label7.pack()


                if text == 'R':
                    if computer_choice == "R":
                        self.draw=self.draw+1
                        label8 = Label(game, text= "Match Draw" )
                        label8.after(2000 , lambda: label8.destroy())
                        label8.pack()
                    elif computer_choice == "P":
                        self.ccount=self.ccount+1
                        label9 = Label(game, text= "computer won" )
                        label9.after(2000 , lambda: label9.destroy())
                        label9.pack()
                    else:
                        self.ycount=self.ycount+1
                        label10 = Label(game, text= "You won" )
                        label10.after(2000 , lambda: label10.destroy())
                        label10.pack()

         



        # if user choose Paper as "P"

                elif text == 'P':

                    if computer_choice == 'P':
                        self.draw=self.draw+1
                        label11 = Label(game, text= "Match Draw" )
                        label11.after(2000 , lambda: label11.destroy())
                        label11.pack()
                    elif computer_choice == 'R':
                        self.ccount=self.ccount+1
                        label12 = Label(game, text= "computer won" )
                        label12.after(2000 , lambda: label12.destroy())
                        label12.pack()
                    else:
                        self.ycount=self.ycount+1
                        label13 = Label(game, text= "You won" )
                        label13.after(2000 , lambda: label13.destroy())
                        label13.pack()

        # if user choose Scissors as "S"

                else:
                    if computer_choice == 'S':
                        self.draw=self.draw+1
                        label14 = Label(game, text= "Draw" )
                        label14.after(2000 , lambda: label14.destroy())
                        label14.pack()
                    elif computer_choice == 'R':
                        self.ycount=self.ycount+1
                        label15 = Label(game, text= "You won" )
                        label15.after(2000 , lambda: label15.destroy())
                        label15.pack()
                    else:
                        self.ccount=self.ccount+1
                        label16 = Label(game, text= "Computer won" )
                        label16.after(2000 , lambda: label16.destroy())
                        label16.pack()
                        
                self.pwin=(self.ycount/self.total)*100
                self.ploose=(self.ccount/self.total)*100
                self.pdraw=(self.draw/self.total)*100
                
                label17 = Label(game, text= "You won="+str(self.ycount)+"computer won="+str(self.ccount)+"Draw="+str(self.draw) )
                label17.after(2000 , lambda: label17.destroy())
                label17.pack()
                
                label18 = Label(game, text= "You won %="+str(self.pwin)+"computer won %="+str(self.ploose)+"Draw%="+str(self.pdraw) )
                label18.after(2000 , lambda: label18.destroy())
                label18.pack()
                
                return           
                        
                
        game=Tk()
        e=Entry(game, width=30,bg='yellow')
        button = Button(game,text='Enter choise',command= lambda:logic1(e,game),bg='green')
        button.pack(side='right')

        
        button1 = Button(game,text='Quit',command= lambda:quit(game),bg='green')
        button1.pack(side='bottom')
        
        label1 = Label(game, text= "Type your choice for Rock R, for paper P ,  for scissors S  : " )
        label1.pack()
        
        e.pack()
        
    def start_app(self):
        
        
        welcome = tkFont.Font(family='arial', size=55)
        welcome = Label(self.obj, text='Rock paper  \n\n\n',font=welcome,background="green")
        welcome.pack(fill='both', expand=True, anchor=CENTER)
        
        
        
        button = Button(self.obj,text='Lets play',command= lambda: self.letsplay())
        button.pack()
        
                   
        
if __name__ == "__main__": 
    object1 = Tk()
    object2 = app(object1)
    object2.start_app()
    object1.mainloop()        
