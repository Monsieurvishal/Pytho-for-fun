#I have used functional programming model

import requests #HTTPS requests
import json# To deal with json data

from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    
    url = 'https://www.fast2sms.com/dev/bulk'
    
    # dictionary to change
    
    params = {
        'authorization': '******api key******',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
             }
    response = requests.get(url, params=params) # returns a json file
    
    dict1 = response.json() # convert the json file into dictionary

    return dict1.get('return') #only send the return key from the returned dictionary


def button_click():
    
    num = textNumber.get() #Get number from GUI
    
    msg = textMsg.get("1.0", END)  # Get message from the user
    
    r = send_sms(num, msg) #returns if the message is sent or not
    
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


# Creating GUI
root = Tk()

root.title("Message Sender ")
root.geometry("400x550")

font = ("Helvetica",10, "bold")

textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)

textMsg = Text(root)
textMsg.pack(fill=X)

sendBtn = Button(root, text="SEND SMS", command=button_click)
sendBtn.pack()

root.mainloop()
