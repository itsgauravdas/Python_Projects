from tkinter import *
import datetime
import time
import os 
import pygame

root=Tk()

#Set the sound
pygame.mixer.init(42050,16,2048)
alarm_sound=pygame.mixer.Sound('HeyYa.mp3')


def alarm(set_alarm):
    while True:
        time.sleep(1)
        current_time=datetime.datetime.now().time()
        current_time=str(current_time)
        current_time=current_time[:5]
        if current_time==set_alarm:
            print("Time to wake up")
            # os.system("start HeyYa.mp3")
            pygame.mixer.Sound.play(alarm_sound,loops=-1)
            
            break
def actual_time():
    set_alarm=f"{hour.get()}:{minute.get()}"
    set_alarm=str(set_alarm)
    alarm(set_alarm)
    

root.title("Alarm Clock")
root.geometry("350x200")
root.resizable(False,False)

hour=StringVar()
minute=StringVar()

Label(root,text="Hour Min",font="Bold").place(x=10)

hourTime=Entry(root,textvariable=hour,bg="lightblue",fg="black",font="Arial",width=5).place(x=10,y=30)
minuteTime=Entry(root,textvariable=minute,bg="lightblue",fg="black",font="Arial",width=5).place(x=50,y=30)
Label(root,text="Enter time in 24 hour format.",bg="pink",fg="black",font="Arial").place(x=10,y=120)
set=Button(root,text="Set Alarm",fg="black",width=10,command=actual_time,relief=RAISED).place(x=10,y=70)

    
    
root.mainloop()