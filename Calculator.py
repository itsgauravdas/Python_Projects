from tkinter import *
import math as m

# Title of the application as simple calculator
root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg='White', bg='Black')
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)


# User-defined functions for operations

def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)


def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''
    try:
        if text == 'deg':
            result = str(m.degrees(float(no)))
        elif text == 'sin':
            result = str(m.sin(float(no)))
        elif text == 'cos':
            result = str(m.cos(float(no)))
        elif text == 'tan':
            result = str(m.tan(float(no)))
        elif text == 'lg':
            result = str(m.log10(float(no)))
        elif text == 'ln':
            result = str(m.log(float(no)))
        elif text == 'Sqrt':
            result = str(m.sqrt(float(no)))
        elif text == 'x!':
            result = str(m.factorial(int(float(no))))  # converting to integer
        elif text == '1/x':
            result = str(1 / (float(no)))
        elif text == 'pi':
            result = str(m.pi if no == "" else float(no) * m.pi)
        elif text == 'e':
            result = str(m.e if no == "" else m.e ** float(no))
    except ValueError:
        result = "Error"

    e.delete(0, END)
    e.insert(0, result)


def clear():
    e.delete(0, END)


def bksps():
    current = e.get()
    e.delete(len(current) - 1, END)


def evaluate():
    try:
        ans = e.get()
        ans = eval(ans)
        e.delete(0, END)
        e.insert(0, ans)
    except:
        e.delete(0, END)
        e.insert(0, "Error")


# Button arrangement

buttons = [
    ('log', 2, 0), ('deg', 2, 1), ('sin', 2, 2), ('cos', 2, 3), ('tan', 2, 4),
    ('ln', 1, 1), ('(', 1, 2), (')', 1, 3), ('C', 1, 4),
    ('Sqrt', 3, 0), ('e', 3, 1), ('^', 3, 2), (' % ', 3, 3), ('/', 3, 4),
    ('x!', 4, 0), ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), ('X', 4, 4),
    ('1/x', 5, 0), ('4', 5, 1), ('5', 5, 2), ('6', 5, 3), ('-', 5, 4),
    ('pi', 6, 0), ('1', 6, 1), ('2', 6, 2), ('3', 6, 3), ('+', 6, 4),
    ('.', 7, 1), ('0', 7, 2), ('=', 7, 3)
]

for (text, row, col) in buttons:
    if text in {'log', 'deg', 'sin', 'cos', 'tan', 'ln', 'Sqrt', 'x!', '1/x', 'pi', 'e'}:
        button = Button(root, text=text, padx=24, pady=10, relief=RAISED, bg="Black", fg="White")
        button.bind("<Button-1>", sc)
    elif text == "C":
        button = Button(root, text=text, padx=29, pady=10, relief=RAISED, bg="Dark Red", fg="White", command=clear)
    elif text == "DEL":
        button = Button(root, text=text, padx=24, pady=10, relief=RAISED, bg="Dark Red", fg="White", command=bksps)
    elif text == "=":
        button = Button(root, text=text, padx=29, pady=10, relief=RAISED, bg="Dark Orange", fg="Black", command=evaluate)
    else:
        button = Button(root, text=text, padx=29, pady=10, relief=RAISED, bg="Grey" if text.isdigit() else "Yellow",
                        fg="White" if text.isdigit() else "Black", command=lambda t=text: click(t))
    button.grid(row=row, column=col)

root.mainloop()
