# I have used functonal programming concept here


from tkinter import Tk , HIDDEN , NORMAL , Canvas
from  speechrecognition.speak import voicemodule

def toggle_eyes():
    current_color = c.itemcget(eye_left,'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left , 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left , state = new_state)
    c.itemconfigure(pupil_right , state = new_state)
    c.itemconfigure(eye_left , fill = new_color)
    c.itemconfigure(eye_right , fill = new_color)

def blink():
    toggle_eyes()
    win.after(250,toggle_eyes)
    win.after(3000,blink)

def toggle_pupils():
    if not c.crossed_eyes:
        c.move(pupil_left , 10,-5)
        c.move(pupil_right , -10,-5)
        c.crossed_eyes = True
    else:
        c.move(pupil_left , -10,5)
        c.move(pupil_right , 10,5)
        c.crossed_eyes = False

def talk(event):
    
    if(20<= event.x and event.x <= 350) and (20<= event.y and event.y <= 350):
        a=voice_module()
        a.speech_to_text()
    return 



win = Tk()

c = Canvas(win , width=400 , height=400)
c.configure(bg='dark blue' , highlightthickness=0)

c.body_color = 'SkyBlue1'

body = c.create_oval(35,20,365,350,outline=c.body_color , fill=c.body_color)
foot_left = c.create_oval(65,320,145,360 , outline=c.body_color , fill=c.body_color)
foot_right = c.create_oval(250,320,330,360 , outline=c.body_color , fill=c.body_color)

ear_left = c.create_polygon(75,80,75,10,165,70,outline=c.body_color , fill=c.body_color)
ear_right = c.create_polygon(255,45,325,10,320,70,outline=c.body_color , fill=c.body_color)

eye_left = c.create_oval(130,110,160,170,outline='black' , fill='white')
pupil_left = c.create_oval(140,145,150,155,outline='black' , fill='black')
eye_right = c.create_oval(230,110,260,170,outline='black' , fill='white')
pupil_right = c.create_oval(240,145,250,155,outline='black' , fill='black')

mouth_normal = c.create_line(170,250,200,272,230,250,smooth=1 , width=2 , state=NORMAL)
c.pack()


c.bind('<Motion>' , talk)


c.crossed_eyes = False
c.tonque_out = False
c.happy_level = 10

win.after(1000,blink)
win.mainloop()
