from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from googletrans import Translator
from tkinter import messagebox 

root=tk.Tk()
root.title('Language Translator')
root.geometry('530x330')
root.maxsize(530,330)
root.maxsize(530,330)

def translator():
    language_1=t1.get("1.0","end-1c")
    c1=choose_language.get()
    
    if language_1 == '':
        messagebox.showerror('Langugage translator','please fille the box')
    else:
        t2.delete(1.0,"end-1c")
        translator = Translator()
        output = translator.translate(language_1,dest=c1)
        t2.insert('end',output.text)
        
        
def clear():
    t1.delete(1.0,'end')
    t2.delete(1.0,'end')

auto_detect_language = tk.StringVar()
auto_detect = ttk.Combobox(
    root,
    width=20,
    textvariable = auto_detect_language,
    state='readonly',
    font=('verdana',10,'bold')
)

auto_detect['values']=('Auto Detect', )

auto_detect.place(x=30,y=70)
auto_detect.current(0)

language_selected=tk.StringVar()
choose_language=ttk.Combobox(
    root,
                               width=20,
                               textvariable=language_selected,
                               state='readonly',
                               font=('verdana', 10, 'bold')
)

choose_language['values']=('Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    ' Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    ' Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    ' Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
    )

choose_language.place(x=290, y=70)
choose_language.current(0)

t1=Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=100)
t2=Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=200)

button = Button(root,
                text="Translate",
                relief=RIDGE,
                borderwidth=3,
                font=('verdana', 10, 'bold'),
                cursor="hand2",
                foreground='Green',
                command=translator)
button.place(x=150, y=280)

clear = Button(root,
               text="Clear",
               relief=RIDGE,
               borderwidth=3,
               font=('verdana', 10, 'bold'),
               cursor="hand2",
               foreground='Red',
               command=clear)
clear.place(x=280, y=280)

root.mainloop()
