# I have used object OOP concept here

import pyttsx3
import speech_recognition as s

class voicemodule():
    
    def __init__(self):
        self.x=0
        
    def text_to_speech(self,text):
        #engine connects us to hardware
        eng= pyttsx3.init()#Engine created
        eng.say(text)#Runn for small time
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        eng.setProperty('voice', voice_id) 
        eng.runAndWait()
        return

    
    def speech_to_text(self):
        r=s.Recognizer()
        with s.Microphone() as source:
            print("listening....")
            audio= r.listen(source)
            print("Done listening...")
            print(r.recognize_google(audio))
            self.text_to_speech(r.recognize_google(audio))
            return
