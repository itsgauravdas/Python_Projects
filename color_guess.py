import random
import tkinter

colors_name = ['Red', 'White', 'Yellow', 'Pink',
               'Blue', 'Black', 'Brown', 'Purple', 'Green', 'Cyan']

score = 0
time_left = 60 

def start_game(play):
    if time_left == 60:
        countdown()
    change_color()
    
def change_color():
    global score 
    global time_left 
    if time_left > 0:
        e.focus_set()
        if e.get() == colors_name[1].lower():
            score+=1
        e.delete(0, tkinter.END)
        random.shuffle(colors_name)
        label.config(fg=str(colors_name[1]), text=str(colors_name[0]))
        scoreLabel.config(text="Score: "+str(score))
        
def countdown():
    global time_left
    if time_left>0:
        time_left-=1
        timeLabel.config(text="Time left: " + str(time_left))
        timeLabel.config(1000, countdown)
        
        
root=tkinter.Tk()
root.title("The ColorGuess")
root.geometry("600x400")

instruce = tkinter.Label(root, text="Which Color?", font=("san-serif", 30))
instruce.pack()
scoreLabel=tkinter.Label(root, text="Time Left: "+ str(time_left), font=("san-serif", 18))
scoreLabel.pack()
timeLabel=tkinter.Label(root, text="Time Left: "+ str(time_left), font=("san-serif", 18))
timeLabel.pack()

label=tkinter.Label(root, font=("san-serif", 60))
label.pack()

e=tkinter.Entry(root)
root.bind('<Return>', start_game)
e.pack()
e.focus_set()
"""
e.focus_set():
Sets the focus to the entry widget, 
allowing the user to start typing without 
needing to click on it

"""


root.mainloop()