from tkinter import *
from tkinter import messagebox 
from PyDictionary import PyDictionary

root = Tk()
root.title("Dictionary")
root.geometry("500x400")

dictionary = PyDictionary()

def getMeaning():
    word_input = word.get().strip()
    if not word_input:
        messagebox.showinfo("Error", "Please enter a valid word")
        return 
    response = dictionary.meaning(word_input)
    if response:
        if 'Noun' in response:
            meaning = response['Noun'][0]
        elif 'Verb' in response:
            meaning = response['Verb'][0]
        elif 'Adjective' in response:
            meaning = response['Adjective'][0]
        else:
            meaning = "Meaning not found for the given word."
            
    else:
        meaning = "Invalid word or network issue."
    
    meaning_label.config(text = meaning)
    
heading_label = Label(root, text="DICTIONARY", font=(
    "Helvetica", 35, "bold"), foreground='Blue')
heading_label.config(anchor=CENTER)
heading_label.pack(pady=10)

frame = Frame(root)
Label(frame, text="Enter word", font=("Helvetica", 35 ,"bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica", 35 ,"bold"))
word.pack(padx=10)
frame.pack()

search_button = Button(root, text="Search Word", font=("Helvetica 35 bold"), relief=RIDGE,borderwidth=3, cursor="hand2",foreground="green"
                       ,command=getMeaning)
search_button.config(anchor=CENTER)
search_button.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning : ",font=("Helvetica", 35,"bold")).pack(side=LEFT)
meaning_label = Label(frame1, text="",font=("Helvetica", 35,"bold"))
meaning_label.pack(pady=5)
frame1.pack(pady=10)

root.mainloop()