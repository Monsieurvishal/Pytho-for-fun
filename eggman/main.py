from tkinter import Tk,HIDDEN , NORMAL , Canvas


win=Tk()


c = Canvas(win , width=400 , height=400)
c.configure(bg='dark blue' , highlightthickness=0)
c.create_text(200,10,fill="white",font="Times 20 italic bold",text="I am egg man, I am your pet")
c.update
coord = 150 ,130, 250, 230


body = c.create_oval(130,30,270,260,outline='black', fill='white')
arc = c.create_arc(coord, start=180, extent=180,style='arc',outline='black', width=3)

eye_left = c.create_oval(130,110,160,170,outline='black' , fill='white')
pupil_left = c.create_oval(140,145,150,155,outline='black' , fill='black')
eye_right = c.create_oval(230,110,260,170,outline='black' , fill='white')
pupil_right = c.create_oval(240,145,250,155,outline='black' , fill='black')

c.pack()


win.mainloop()
