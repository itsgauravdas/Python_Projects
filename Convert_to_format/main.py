import tkinter
import os 
import sys
from PIL import Image 

def converter():
    
    x=entry.get()
    y=name_var1.get()
    z=name_var2.get()
    
    input_file=x+""+y
    print(input_file)
    
    
    if len(x) > 0:
        if os.path.exists(input_file):
            try:
                im=Image.open(input_file)
                target_name = x + z
                rgb_im = im.convert('RGB')
                rgb_im.save(target_name)
                
                result_label.set(f"Save as : {target_name}")
            except Exception as e:
                result_label.set(f"Error : {e}")
        else:
            
            result_label.set("Not found") 
    else:
       result_label.set("Usage: convert2jpg.py <file>")
       
extensions=['.pdf','.jpeg','.json','.text','.png','.docx']

root = tkinter.Tk()

root.title("Convert to jpg")
root.geometry("500x500")

lab=tkinter.Label(root, text="Enter file name (without extension) ", font=("Red",20))
lab.pack(pady=50)

name_var=tkinter.StringVar()
entry=tkinter.Entry(root,textvariable=name_var,font=('calibre',15,'normal'))
entry.pack(pady=10)


name_var1=tkinter.StringVar()
name_var1.set("Select Format") 
tkinter.Label(root,text="Converted from :").pack()
menu=tkinter.OptionMenu(root,name_var1,*extensions).pack(pady=10)

name_var2=tkinter.StringVar()
name_var2.set("Select Format") 
tkinter.Label(root,text="Converted to :").pack()
menu=tkinter.OptionMenu(root,name_var2,*extensions).pack(pady=10)

#Button
button = tkinter.Button(root,text="clink on ", command=converter).pack(pady=20)


#Output
result_label=tkinter.StringVar()
tkinter.Label(root,textvariable=result_label,font=("Arial", 12), fg="green").pack(pady=10)

tkinter.Button(root,text="Exit", font=("Arial", 12),fg="Red",width=15, height=2,command=root.destroy).pack()
root.mainloop()