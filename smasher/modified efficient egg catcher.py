from itertools import cycle
from random import randrange
from tkinter import Tk , Canvas , messagebox , font

canvas_width = 900
canvas_height = 800

win = Tk()
win.title("Vishal's catcher Game")
c = Canvas(win , width = canvas_width ,  height = canvas_height , background = 'light green')
c.pack()

color_cycle = cycle(['light blue' , 'light pink' , 'light yellow','light green' , 'red', 'blue' , 'green','black'])
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 50
egg_interval = 800

catcher_color = 'black'
catcher_width = 300
catcher_height =300
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height -catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=3)

score = 0
score_text = c.create_text(10,10,anchor='nw' , font=('Arial',18,'bold'),fill='darkblue',text='Score : ' + str(score))

lives_remaning = 20
lives_text = c.create_text(canvas_width-10,10,anchor='ne' , font=('Arial',18,'bold'),fill='darkblue',text='Lives : ' + str(lives_remaning))

eggs = []

def create_eggs():
    x = randrange(10,800)
    y = 40
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    win.after(egg_interval,create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        c.move(egg,0,10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    win.after(egg_speed,move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaning == 0:
        messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
        win.destroy()

def lose_a_life():
    global lives_remaning
    lives_remaning -= 1
    c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))

def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    win.after(100,catch_check)

def increase_score(points):
    global score ,lives_remaning 
    score += points
    if(score==1000 or score==5000 or score==10000 or score==20000 or score==30000 ):
        lives_remaning =20
        c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))
    if score == 100000:
        messagebox.showinfo('you win!\n Winner winner chicken dinner' , 'Final Score : ' + str(score))
        win.destroy()
    
    c.itemconfigure(score_text , text='Score : ' + str(score))

def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher,-20,0)
        
def move_top(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2 > 0:
        c.move(catcher,0,-20)
        
def move_bottom(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if y2 < canvas_height:
        c.move(catcher,0,+20)

def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher,20,0)

c.bind('<Left>' , move_left)
c.bind('<Right>' , move_right)
c.bind('<Up>' , move_top)
c.bind('<Down>' , move_bottom)
c.focus_set()

win.after(10,create_eggs)
win.after(1000,move_eggs)
win.after(1000,catch_check)

win.mainloop()
