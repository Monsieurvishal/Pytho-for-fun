from itertools import cycle # For iteration
from random import randrange # For random egg falling
from tkinter import Tk , Canvas , messagebox , font

canvas_width = 900 #Height and width of the canvas if you want to change the canvas you can change here globally
canvas_height = 500

win = Tk()    #our main window object
win.title("Vishal's Egg catcher Game")


''' Canvas code'''
c = Canvas(win , width = canvas_width ,  height = canvas_height , background = 'deep sky blue')
c.create_rectangle(-5, canvas_height - 100 , canvas_width + 5 , canvas_height + 5 , fill='sea green', width=0)
c.create_oval(-80,-80,120,120,fill='red' , width=0)
c.pack()

color_cycle = cycle(['light blue' , 'light pink' , 'light yellow','light green' , 'red', 'blue' , 'green','black'])
egg_width = 45
egg_height = 55''' these variables will be used by the functions'''
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95

catcher_color = 'black'
catcher_width = 200
catcher_height = 200'''To place the catcher nearly in the center and match the cordinate of the arc'''
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height -catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(catcher_start_x ,catcher_start_y ,catcher_start_x2,catcher_start_y2 , start=200 , extent = 140 , style='arc' , outline=catcher_color , width=3)

score = 0
score_text = c.create_text(10,10,anchor='nw' , font=('Arial',18,'bold'),fill='darkblue',text='Score : ' + str(score))

lives_remaning = 3
lives_text = c.create_text(canvas_width-10,10,anchor='ne' , font=('Arial',18,'bold'),fill='darkblue',text='Lives : ' + str(lives_remaning))


''' This game works on the functional programming
    Functions are defined below which is the heartbeat of this game'''
    
eggs = [] #Store the created eggs

def create_eggs():
    x = randrange(10,740)
    y = 40
    '''Eggs areoval in shape oval created by x0 x2 y0 y1''''
    
    new_egg = c.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    ''' after every 4 seconds'''
    
    win.after(egg_interval,create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)# this gets the co ordinate once the GUI is live
        c.move(egg,0,10) #pushes the egg to down
        if egg_y2 > canvas_height: #if egg hits the canvas height
            egg_dropped(egg) #call the droped egg function
    win.after(egg_speed,move_eggs) #repeat the same aftwe some seconds

def egg_dropped(egg): #checks if the player has the eligibility to continue
    eggs.remove(egg) # if it hits the canvashe has to remove that egg from the list
    c.delete(egg)#delete the egg from the canvas
    lose_a_life()
    if lives_remaning == 0:
        messagebox.showinfo('GAME OVER!' , 'Final Score : ' + str(score))
        win.destroy()

def lose_a_life():
    global lives_remaning #the change should reflect Globally
    lives_remaning -= 1
    c.itemconfigure(lives_text , text='Lives : ' + str(lives_remaning))

def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2  < catcher_x2 and catcher_y2 - egg_y2 < 40: 
            # this checks if the egg has come near to the bowl(catcher)
            
            eggs.remove(egg)
            c.delete(egg)#delete the egg from the canvas
            increase_score(egg_score)
    win.after(100,catch_check)

def increase_score(points): # increasing the points
    global score , egg_speed , egg_interval # changes has to be reflected globally
    score += points # increase the score
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text , text='Score : ' + str(score))#to item configure to change once the GUI is live
#movement control in GUI

def move_left(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher,-20,0)

def move_right(event):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher,20,0)
#keyboard functions to  trigger our functions

c.bind('<Left>' , move_left)
c.bind('<Right>' , move_right)

c.focus_set()

#functions which monitered after some time

win.after(1000,create_eggs)
win.after(1000,move_eggs)
win.after(1000,catch_check)

win.mainloop()
