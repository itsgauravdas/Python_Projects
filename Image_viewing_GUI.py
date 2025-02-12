from tkinter import * 
from PIL import Image, ImageTk
import os 

root = Tk()
root.geometry("600x600")

def resize_image(root, copy_image, label1):
    new_height = 600
    new_width = 600 
    image = copy_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image = photo 

def next():
    global n     
    global itemslist 
    n = (n+1) % len(itemslist)
    img1 = itemslist[n]
    
    image = Image.open(path+r"'\'"+img1)
    copy_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label1 = Label(root, image=photo)
    label1.bind('<configure>', resize_image(root, copy_image, label1))
    label1.pack()
    
    
    
    

    


root.mainloop()