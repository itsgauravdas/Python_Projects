import os.path
# python program to generate random
# password using Tkinter module 
import random 
import pyperclip 
import tkinter
from tkinter import *
from tkinter.ttk import * 

# Function for calculation of password 
def low():
    entry.delete(0,END)
    
    # Get the length of password 
    length =var1.get()
    
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password=""
    
    # if strength selected is low 
    
    if var.get() == 1:
        for i in range(0,length):
            password=password + random.choice(lower)
        return password
    
    # is strength selected is medium
    
    elif var.get() ==0:
        for i in range(0,length):
            password=password+ random.choice(digits)
        return password
    
    # if strength selected is strong 
    elif var.get() == 3:
        for i in range(0,length):
            password=password+random.choice(digits)
        return password
    
    else:
        print("Please choose an option ")
        

# Function for generation of password 

def generate():
    password1=low()
    entry.insert(10,password1)
    
# Function of copying password to clipboard
def copy1():
    random_password=Entry.get()
    pyperclip.copy(random_password)
    
def checkExistence():
    if os.path.exists("info.txt"):
        pass 
    else:
        with open('info.txt','w') as file:
            file.close()
            
def appendNew():
    with open('info.txt','a') as file:
        userName=entry1.get()
        website=entry2.get()
        Random_password=entry.get()
        usrnm="UserName: " + userName + "\n"
        pwd="Password: " + Random_password + "\n"
        web="Website: " + website + "\n"
        file.write('-----------------------------------------')
        file.write("\n")
        file.write(usrnm)
        file.write(pwd)
        file.write(web)
        file.write('------------------------------------------')
        file.write("\n")
        file.close()
        
        with open('info.txt','a') as file:
            pass 
#-----------------------------------------------------------------


def readPassword():
    with open('info.txt','r') as file:
        content=file.read()
        file.close()
        output_label.config(text=content)
        output_label.grid(row=5,column=1)
        Output_frame.grid(row=5,column=1)
        # print(content)
        
        
        


        
# Main function
checkExistence()
# Create GUI window 
root=Tk()
var=IntVar()
var1=IntVar()

root.title("Python Password Manager")

c_label=Label(root,text="Length")
c_label.grid(row=1)

# create Buttons Copy which will copy 
# password to clipboard and Generate 
# which will generate the password 

copy_button=Button(root,text="Copy",command=copy1)
copy_button.grid(row=0,column=2)

generate_button=Button(root,text="Generate",command=generate)
generate_button.grid(row=0,column=3)

# Radio Buttons for deciding the 
# strength of password 
# Default strength is Medium 

radio_low=Radiobutton(root,text="Low",variable=var, value=1)
radio_low.grid(row=1,column=2,sticky="E")
radio_middle=Radiobutton(root,text="Medium",variable=var,value=3)
radio_middle.grid(row=1,column=3,sticky="E")
radio_strong=Radiobutton(root,text="Strong",variable=var,value=3)
radio_strong.grid(row=1,column=4,sticky="E")
combo=Combobox(root,textvariable=var1)


# Combo Box for length of your password 
combo['values']=(8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32, "Length") 

combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1,row=1)

# create label and entry to show 
# password generated 
userName=Label(root,text="Enter user name here")
userName.grid(row=2)
entry1=Entry(root)
entry1.grid(row=2,column=1)

# create label and entry to show 
# password generated 

website=Label(root,text="Enter website address here")
website.grid(row=3)
entry2=Entry(root)
entry2.grid(row=3,column=1)

Random_password=Label(root,text="Generate password")
Random_password.grid(row=4)
entry=Entry(root)
entry.grid(row=4,column=1)

save_button=Button(root,text="Save",command=appendNew)
save_button.grid(row=2,column=2)
show_button=Button(root,text="Show all password",command=readPassword)
show_button.grid(row=2,column=3)

#---------------------
Output_frame=tkinter.Frame(root,highlightbackground='Light Green', highlightthickness=5) #Make the output in a frame
output_label=tkinter.Label(Output_frame,text="",font=('Georgia',15))
output_label.pack(padx=10)


root.mainloop()
