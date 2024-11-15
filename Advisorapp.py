import requests 
import tkinter as tk 
from tkinter import messagebox 

def advice():
    try:
        res = requests.get("https://api.adviceslip.com/advice").json()
        advice_text.set(res["slip"]["advice"])
        return advice_text
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Failed to fetch advice. Please check your internet connection.")

#Create the mail window 

root=tk.Tk()
root.title('Random Advisor Application')

#Create and Configure Widgets
advice_text=tk.StringVar()
advice_label=tk.Label(root, textvariable=advice_text,
                      wraplength=400, font=("Arial", 14))

get_advice_button=tk.Button(root, text="Get Advice", command=advice)

#Pack Widgets
advice_label.pack(pady=20)
get_advice_button.pack(pady=10)

#Initial advice fetching
advice()

#Run the main loop
root.mainloop()