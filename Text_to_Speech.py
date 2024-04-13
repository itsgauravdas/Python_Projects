#----tkinter is got GUI 
import tkinter as tk 
from tkinter import * 
#---pyttsx3 is for voice
import pyttsx3 


engine=pyttsx3.init()


#--This function taking the input and generating the voice
def speaknow():
    # engine.say(textv.get())
    engine.say(textv.get())
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Victoria')
    
    engine.runAndWait()
    


#--This is the object for Tk() class which present in tkinter library
root=Tk()


#--creating a string variable 
textv=StringVar()

#-----Creatring the frame 
obj=LabelFrame(root,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

#--------------Creating the label
lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)


#---adding the data entry field
text=Entry(obj,textvariable=textv,font= 30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)


#--Adding the button
btn=Button(obj,text="Speak",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10,pady=(10,0))

#--------- Add heading 
root.title("Text to speech")
#--define the size
root.geometry("600x400")
root.resizable(False,False) 
#--Holding the window  
root.mainloop()
