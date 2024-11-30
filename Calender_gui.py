from tkinter import *
import calendar 

def showCal():
    
    box=Tk()
    
    box.title("Calender from the year")
    box.geometry("550x600")
    find_year = int(year_field.get())
    
    first_label=Label(box, text='CALENDER', bg='dark gray', font=("times", 28, "bold"))
    first_label.grid(row=1,column=1,pady=10)
    
    box.config(background="white")
    
    cal_data= calendar.calendar(find_year)
    cal_year=Label(box, text=cal_data, font="consolas 10 bold", justify=LEFT)
    cal_year.grid(row=2,column=1,padx=10)
    exit_button = Button(box, text="CLOSE", bg="peach puff", command=box.destroy)
    exit_button.grid(row=3, column=1, pady=10)
    
    box.mainloop()

if __name__  == "__main__" :
    gui=Tk()
    gui.config(background="misty rose")
    gui.title("CALENDER")
    gui.geometry("250x250")
    cal=Label(gui, text="CALENDER", bg="lavender", font=("Helvetica", 28, "bold", "underline"))
    year=Label(gui, text="Enter Year", bg="peach puff", padx=10,pady=10)
    year_field=Entry(gui)
    show=Button(gui, text="Show calender", fg="Black", bg="lavender", command=showCal)
    exit=Button(gui, text="CLOSE", bg="peach puff", command=exit)
    cal.grid(row=1,column=1)
    year.grid(row=3,column=1)
    year_field.grid(row=4,column=1)
    show.grid(row=5,column=1)
    exit.grid(row=7,column=1)
    gui.mainloop()
showCal()