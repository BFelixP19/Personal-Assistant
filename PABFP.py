#This is an online speech recognition personal assistant using Google Speech Recoginiton
#Packages required to use this application are "SpeechRecognition" and "pyaudio"

#List of commands that can be performed using this applcation:
#Find Your IP
#Find Your MAC
#Open an application(ONLY FOR CERTAIN APPLICATIONS)
#Go to a particular directory
#Serach online in google
#Display time, weather and date
#Restart, Shutdown or Logout commands
#Turn on and off Wi-Fi
#Close the application



import os
import speech_recognition as sr
from tkinter import Button, Tk, HORIZONTAL
from tkinter import *
from tkinter.ttk import Progressbar
import time
import threading
from datetime import datetime
from datetime import date


class MonApp(Tk):
    n = 0
    while n < 100:

        def __init__(self):
            super().__init__()
            self.title("Bot Assistant")
            self.configure(background='black')
            self.geometry("500x500")
            self.btn1 = Button(self, text='SPEAK', command=self.traitement)
            self.btn1.place(x=205, y=250)
            label1=Label(self,text="Personal Assistant",relief='solid',width=20,font=("arial",19,"bold"))
            label1.place(x=90,y=53)
            self.progress = Progressbar(self, orient=HORIZONTAL, length=1000, mode='indeterminate')

        def traitement(self):

            def real_traitement():
                self.progress.grid(row=5000, column=0)

                                # Record Audio
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.dynamic_energy_threshold = False
                    r.energy_threshold = 400
                    print("Speak Now")
                    audio = r.listen(source, timeout=5.0)

                try:
                    voice = r.recognize_google(audio)
                    print("Command: " + voice.capitalize())
                except sr.UnknownValueError:
                    print("Given command is not comprehendable")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))

                self.progress.start()
                time.sleep(5)
                self.progress.stop()
                self.progress.grid_forget()




                t = voice
                a = t.lower()
                b = a.split(" ")

                if a == "what is my ip":
                    os.system('ipconfig|findstr IPv4')

                elif a == "what is my mac":
                    os.system("ipconfig/all | findstr Physical")

                elif b[0] == "open":
                    # open chrome
                    os.system("start " + b[1])

                elif b[0] == "go":
                    # go to eg.c drive*
                    c = b[2].upper()
                    os.system("start " + c + ":/")

                elif b[0] == "search":
                    # search for eg.hello
                    f = b[1:]
                    st=" ".join(f)
                    os.system("start chrome google.com/search?q={}".format(st))

                elif a == "what is today's date":
                    today = date.today()
                    print("Today's date:", today)

                elif a == "what's the time":
                    now = datetime.now()
                    dt_string = now.strftime(" %H:%M:%S")
                    print("time =", dt_string)

                elif a == "what is today's whether":
                    os.system("start chrome google.com/search?q=today+weather ")

                elif a == "close bot assistant":
                    print("Thank you for using bot assistant")
                    self.destroy()
                    
                elif a == "shutdown":
                    os.system("shutdown/s")
                    print("your system will be switched off in a minute ")

                elif a == "restart":
                    os.system("shutdown/r")

                elif a == "log off":
                    os.system("shutdown/l")

                elif a == "turn wi-fi on":
                    # administrator permission
                    os.system("netsh interface set interface Wi-Fi enabled")

                elif a == "turn wi-fi off":
                    # administrator permission
                    os.system("netsh interface set interface Wi-Fi disabled")

                else:
                    print("Bot Assistant can't recognize this command at this movement")
                    print("Please try again")

                self.btn1['state'] = 'normal'

            self.btn1['state'] = 'disabled'
            threading.Thread(target=real_traitement).start()
        n = n+1


if __name__ == '__main__':

    app = MonApp()
    app.mainloop()
